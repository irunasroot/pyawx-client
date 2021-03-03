"""
models/utils/__init__.py
Comments: 
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2021, iRunAsRoot
"""

from pyawx.exceptions import ValueNotAllowed


def set_changes(obj, key, value, value_type, limit=None):
    """
    Updates values within the object

    :param obj: The model object
    :param key: The key to update
    :param value: The new value
    :param value_type: The expected type the value should be
    :param limit: A list of values that are allowed
    :return: None
    """
    if limit and value not in limit:
        raise ValueNotAllowed

    if not isinstance(value, value_type):
        raise TypeError

    obj._data[key] = value
    obj._changes[key] = value


def get_endpoint(model):
    """
    Get the endpoint for the model object. If the model is an existing one the
    endpoint will be to that specific endpoint

    :param model: The model
    :type model: subclass of :class:`pyawx.models.mixins.DataModelMixin`
    :return: str
    """
    return model.__endpoint__ if not model.id else f"{model.__endpoint__}/{model.id}"


def delete(model):
    """
    Marks a record as deleted

    :param model: The model
    :type model: subclass of :class:`pyawx.models.mixins.DataModelMixin`
    :return: none
    """

    model.__delete_record__()


def update(model, data):
    """
    Updates a mode with the data provided. Usually comes from the AWX API

    :param model: The model
    :type model: subclass of :class:`pyawx.models.mixins.DataModelMixin`
    :param data: The dict of data to update the object with
    :type data: dict
    :return: None
    """
    model.__update__(**data)


def export(model):
    """
    Exports the data from a model as a dict
    :param model: The model
    :type model: subclass of :class:`pyawx.models.mixins.DataModelMixin`
    :return: dict
    """
    model.__export__()
