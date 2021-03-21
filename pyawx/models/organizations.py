from pyawx.models import types
from pyawx.models.mixins import DataModelMixin
from pyawx.models.utils import set_changes
from pyawx.exceptions import ValueReadOnly


class Organization(DataModelMixin):
    __endpoint__ = "/api/v2/organizations"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param name: Name of this organization.
            :type name: str, required
            :param description: Optional description of this organization.
            :type description: str, default ""
            :param max_hosts: Maximum number of hosts allowed to be managed by this organization.
            :type max_hosts: int, default 0
            :param custom_virtualenv: Local absolute file path containing a custom Python virtualenv to use
            :type custom_virtualenv: str, default ""

        Read Only Attributes:
            :param id: Database ID for this organization.
            :type id: int, readonly
            :param type: Data type for this organization.
            :type type: str, readonly
            :param url: URL for this organization.
            :type url: str, readonly
            :param created: Timestamp when this organization was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this organization was last modified.
            :type modified: datetime, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this organization. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this organization. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this organization. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this organization was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this organization was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this organization. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this organization. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def max_hosts(self):
        """Maximum number of hosts allowed to be managed by this organization. (integer)"""
        return self._data.get("max_hosts")

    @max_hosts.setter
    def max_hosts(self, value):
        set_changes(self, "max_hosts", value, types.INTEGER)

    @property
    def custom_virtualenv(self):
        """Local absolute file path containing a custom Python virtualenv to use (string)"""
        return self._data.get("custom_virtualenv")

    @custom_virtualenv.setter
    def custom_virtualenv(self, value):
        set_changes(self, "custom_virtualenv", value, types.STRING)
