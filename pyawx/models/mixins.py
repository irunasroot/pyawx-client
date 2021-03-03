from copy import deepcopy


class DataModelMixin:
    """
    Base data model structure
    """
    __deleted__ = False

    def __init__(self, **kwargs):
        self._data = deepcopy(kwargs)
        self._changes = dict()
        self._cache = dict()

    def __repr__(self):
        return f"<{self.__class__.__name__} object at {id(self)}>"

    def __export__(self):
        """
        Export of the model ojbect as a dict. This is a copy of the internal
        tracking dict as to prevent model changes
        """
        return deepcopy(self._data)

    def __update__(self, **data):
        """
        Updates a model object
        :param data: data payload from the AWX API
        :return: None
        """
        self._data.update(data)

    @property
    def is_changed(self):
        return True if self._changes else False

    def is_deleted(self):
        return self.__deleted__

    def __delete_record__(self):
        self.__deleted__ = True

    def revert(self, attribute):
        """
        Revert the attribute that had been changed. This pulls from the cached data set when the change was made
            and then removes it and reverses the change.
        :param attribute: The attribute name you want to change
        :type attribute: str
        :return: None
        """
        if attribute in self._changes:
            self._data[attribute] = self._changes.get(attribute)
            del self._changes[attribute]
