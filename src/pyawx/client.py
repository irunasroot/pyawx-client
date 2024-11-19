from base64 import b64encode
from urllib.parse import urlparse

import requests

from pyawx.client_cache import set_client
from pyawx.exceptions import UnauthorizedAccess, UnknownEndpoint
from pyawx.models.mixins import DataModelMixin
from pyawx.models.utils import flush, get_endpoint, update


class _ApiUrl:
    def __init__(self, url):
        self._url = "/".join(urlparse(url)[0:2])

    def endpoint(self, endpoint):
        return f"{self._url}{endpoint}"


class Client:
    """
    Client object for connecting to an AWX instance
    """

    def __init__(self, url, username=None, password=None, token=None):
        """
        Main client API object for connecting to an AWX instance.

        The OAuth token takes precedence over username and password if all three are provided.

        :param url: The base URL of the AWX instance
        :type url: str, required
        :param username: Your AWX username
        :type username: str, optional if token not provided
        :param password: Your AWX password
        :type password: str, optional if token not provided
        :param token: OAuth token
        :type token: str, optional if username and password supplied
        """

        self.url = _ApiUrl(url)
        self._write_back = list()

        self._session = requests.Session()

        if token:
            authorization = "Bearer {0}".format(token)
        elif username and password:
            authorization = (
                f"Basic {b64encode(f'{username}:{password}'.encode()).decode()}"
            )
        else:
            raise ValueError("No username and password or token was supplied")

        self._session.headers.update(
            {"Content-Type": "application/json", "Authorization": authorization}
        )

        _me = self._session.get(self.url.endpoint("/api/v2/me"))

        if _me.status_code in [401, 403]:
            raise UnauthorizedAccess(_me.text)
        elif _me.status_code == 404:
            raise UnknownEndpoint(_me.text)

        # Cache the client so models can access it
        set_client(self)

    def _get(self, model):
        result = self._session.get(self.url.endpoint(get_endpoint(model)))
        return result

    def _post(self, model):
        result = self._session.post(
            self.url.endpoint(f"{model.__endpoint__}"), json=model.export()
        )
        status_code = result.status_code
        result = result.json()

        if status_code == 201:
            update(model, result)

        # TODO: Error handling. Errors come as result["detail"]

    def _put(self, model):
        result = self._session.put(self.url.endpoint(get_endpoint(model)))

        if result.status_code != 201:
            pass

        # TODO: Error handling. Errors come as result["detail"]

    def _delete(self, model):
        result = self._session.delete(self.url.endpoint(get_endpoint(model)))

        if result.status_code != 201:
            pass

        # TODO: Error handling. Errors come as result["detail"]

    def get_data(self, model):
        """
        Load model object

        :param model: The model object that is being requested
        :type model: class of
            | :class:`pyawx.models.projects.Project`
        :return: List of requested objects
        """

        items = list()

        results = self._session.get(self.url.endpoint(get_endpoint(model)))

        if results.status_code != 200:
            raise Exception(results.json()["detail"])

        results = results.json()

        for item in results["results"]:
            items.append(model(internal_=True, **item))

        return items

    def add(self, model):
        if not isinstance(model, DataModelMixin):
            raise ValueError("Model is not a valid pyawx model")
        self._write_back.append(model)

    def add_all(self, models):
        """
        Queue a list of stored models prepared for saving.

        :param models: A list of Data Models
        :type models: list
        :return: None
        """

        if not isinstance(models, list):
            raise ValueError("Object not of type list")

        for model in models:
            self.add(model)

    def commit(self):
        """
        Commits all queued records back to AWX

        :return: None
        """

        for model in self._write_back:
            if model.is_deleted:
                self._delete(model)
            elif model.is_changed:
                self._put(model)
                flush(model)
            else:
                self._post(model)

        self._write_back = list()

    def delete(self, model):
        """
        Marks a record as deleted

        :param model: The model
        :type model: subclass of :class:`pyawx.models.mixins.DataModelMixin`
        :return: model
        """

        model.__delete_record__()
        self.add(model)
