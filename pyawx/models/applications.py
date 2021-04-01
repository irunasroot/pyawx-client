from pyawx.models import types
from pyawx.models.mixins import DataModelMixin
from pyawx.models.utils import set_changes
from pyawx.exceptions import ValueReadOnly


class Application(DataModelMixin):
    __endpoint__ = "/api/v2/applications"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param name: Name of this application.
            :type name: str, required
            :param description: Optional description of this application.
            :type description: str, default ""
            :param client_type: Set to Public or Confidential depending on how secure the client device is. (choice)
                | confidential: Confidential
                | public: Public
            :type client_type: str, choice, required
            :param redirect_uris: Allowed URIs list, space separated (string)
            :type redirect_uris: str, default ""
            :param authorization_grant_type: The Grant type the user must use for acquire tokens for this application.
                | authorization-code: Authorization code
                | password: Resource owner password-based
            :type authorization_grant_type: str, choice, required
            :param skip_authorization: Set True to skip authorization step for completely trusted applications.
            :type skip_authorization: bool, Default False
            :param organization: Organization containing this application.
            :type organization: int, required

        Read Only Attributes:
            :param id: Database ID for this application.
            :type id: int, readonly
            :param type: Data type for this application.
            :type type: str, readonly
            :param url: URL for this application.
            :type url: str, readonly
            :param created: Timestamp when this application was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this application was last modified.
            :type modified: datetime, readonly
            :param client_id: Client ID
            :type client_id: str, readonly
            :param client_secret: Used for more stringent verification of access to an
                application when creating a token
            :type client_secret: str, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this application. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this application. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this application. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this application was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this application was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this application. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this application. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def client_id(self):
        """Client ID"""
        return self._data.get("client_id")

    @client_id.setter
    def client_id(self, value):
        raise ValueReadOnly

    @property
    def client_secret(self):
        """Used for more stringent verification of access to an application when creating a token. (string)"""
        return self._data.get("client_secret")

    @client_secret.setter
    def client_secret(self, value):
        raise ValueReadOnly

    @property
    def client_type(self):
        """Set to Public or Confidential depending on how secure the client device is. (choice)"""
        return self._data.get("client_type")

    @client_type.setter
    def client_type(self, value):
        allowed_values = [
            "confidential",
            "public"
        ]
        set_changes(self, "client_type", value, types.STRING, allowed_values)

    @property
    def redirect_uris(self):
        """Allowed URIs list, space separated (string)"""
        return self._data.get("redirect_uris")

    @redirect_uris.setter
    def redirect_uris(self, value):
        set_changes(self, "redirect_uris", value, types.STRING)

    @property
    def authorization_grant_type(self):
        """The Grant type the user must use for acquire tokens for this application. (choice)"""
        return self._data.get("authorization_grant_type")

    @authorization_grant_type.setter
    def authorization_grant_type(self, value):
        allowed_values = [
            "authorization-code",
            "password"
        ]
        set_changes(self, "authorization_grant_type", value, types.STRING, allowed_values)

    @property
    def skip_authorization(self):
        """Set True to skip authorization step for completely trusted applications. (boolean)"""
        return self._data.get("skip_authorization")

    @skip_authorization.setter
    def skip_authorization(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "skip_authorization", value, types.BOOLEAN, allowed_values)

    @property
    def organization(self):
        """Organization containing this application. (id)"""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.INTEGER)


class Token(DataModelMixin):
    __endpoint__ = "/api/v2/tokens"

    def __init__(self, **kwargs):
        """
         Attributes:
            :param description: Optional description of this application.
            :type description: str, default ""
            :param application: The application
            :type application: int, default ``
            :param scope: Allowed scopes, further restricts user’s permissions.
                Must be a simple space-separated string with
                | read
                | write
                | read write
            :type scope: str, choice, default "write"

         Read Only Attributes:
            :param id: Database ID for this application.
            :type id: int, readonly
            :param type: Data type for this application.
            :type type: str, readonly
            :param url: URL for this application.
            :type url: str, readonly
            :param created: Timestamp when this application was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this application was last modified.
            :type modified: datetime, readonly
            :param user: The user representing the token owner
            :type user: int, readonly
            :param token: The token
            :type token: str
            :param expires: Expiration
            :type expires: datetime, readonly

        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this access token. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this application. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this application. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this application was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this application was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this application. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def user(self):
        """The user representing the token owner (id)"""
        return self._data.get("user")

    @user.setter
    def user(self, value):
        raise ValueReadOnly

    @property
    def token(self):
        """The token"""
        return self._data.get("token")

    @token.setter
    def token(self, value):
        raise ValueReadOnly

    @property
    def application(self):
        """The application"""
        return self._data.get("application")

    @application.setter
    def application(self, value):
        raise ValueReadOnly

    @property
    def expires(self):
        """expires"""
        return self._data.get("expires")

    @expires.setter
    def expires(self, value):
        raise ValueReadOnly

    @property
    def scope(self):
        """
        Allowed scopes, further restricts user’s permissions. Must be a simple space-separated string with
        allowed scopes ['read’, ‘write’]. (string)
        """
        return self._data.get("scope")

    @scope.setter
    def scope(self, value):
        allowed_values = [
            "read",
            "write",
            "read write",
            "write read"
        ]
        set_changes(self, "scope", value, type, allowed_values)
