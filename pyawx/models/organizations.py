from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class Organization(DataModelMixin):
    __endpoint__ = "/api/v2/organizations"

    def __init__(self, **kwargs):
        """
        Organization List

        Attributes:
            :param name: Name of this organization.
            :type name: string, required, default ``
            :param description: Optional description of this organization.
            :type description: string, required, default ""
            :param max_hosts: Maximum number of hosts allowed to be managed by this 
                organization.
            :type max_hosts: integer, required, default 0
            :param custom_virtualenv: Local absolute file path containing a custom Python 
                virtualenv to use
            :type custom_virtualenv: string, required, default "None"

        Read Only Attributes:
            :param id: Database ID for this organization.
            :type id: integer, readonly
            :param type: Data type for this organization.
                | organization: Organization
            :type type: choice, readonly
            :param url: URL for this organization.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this organization was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this organization was last modified.
            :type modified: datetime, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this organization."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this organization."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this organization."""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def related(self):
        """Data structure with URLs of related resources."""
        return self._data.get("related")

    @related.setter
    def related(self, value):
        raise ValueReadOnly

    @property
    def summary_fields(self):
        """Data structure with name/description for related resources.  The output for some objects may be limited 
        for performance reasons."""
        return self._data.get("summary_fields")

    @summary_fields.setter
    def summary_fields(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this organization was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this organization was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this organization."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this organization."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def max_hosts(self):
        """Maximum number of hosts allowed to be managed by this organization."""
        return self._data.get("max_hosts")

    @max_hosts.setter
    def max_hosts(self, value):
        set_changes(self, "max_hosts", value, types.INTEGER)

    @property
    def custom_virtualenv(self):
        """Local absolute file path containing a custom Python virtualenv to use"""
        return self._data.get("custom_virtualenv")

    @custom_virtualenv.setter
    def custom_virtualenv(self, value):
        set_changes(self, "custom_virtualenv", value, types.STRING)
