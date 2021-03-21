from pyawx.models import types
from pyawx.models.mixins import DataModelMixin
from pyawx.models.utils import set_changes
from pyawx.exceptions import ValueReadOnly


class Instance(DataModelMixin):
    __endpoint__ = "/api/v2/instances"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param capacity: Capacity
            :type capacity: integer, readonly
            :param enabled: Enabled
            :type enabled: boolean, readonly
            :param managed_by_policy: Managed by policy
            :type managed_by_policy: boolean, readonly

        Read Only Attributes:
            :param id: Database ID for this instance.
            :type id: int, readonly
            :param type: Data type for this instance.
            :type type: str, readonly
            :param url: URL for this instance.
            :type url: str, readonly
            :param uuid: Uuid
            :type uuid: str, readonly
            :param hostname: Hostname
            :type hostname: str, readonly
            :param created: Timestamp when this instance was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this instance was last modified.
            :type modified: datetime, readonly
            :param capacity_adjustment: Capacity adjustment
            :type capacity_adjustment: float, readonly
            :param version: Version
            :type version: float, readonly
            :param consumed_capacity: Consumed capacity
            :type consumed_capacity: field, readonly
            :param percent_capacity_remaining: Percent capacity remaining
            :type percent_capacity_remaining: field, readonly
            :param jobs_running: Count of jobs in the running or waiting state that are targeted for this instance
            :type jobs_running: integer, readonly
            :param jobs_total: Count of all jobs that target this instance
            :type jobs_total: integer, readonly
            :param cpu: CPU
            :type cpu: integer, readonly
            :param memory: Memory
            :type memory: integer, readonly
            :param cpu_capacity: Cpu Capacity
            :type cpu_capacity: integer, readonly
            :param mem_capacity: Memory capacity
            :type mem_capacity: integer, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this instance. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this instance. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this instance. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def uuid(self):
        """Uuid"""
        return self._data.get("uuid")

    @uuid.setter
    def uuid(self, value):
        raise ValueReadOnly

    @property
    def hostname(self):
        """Hostname"""
        return self._data.get("hostname")

    @hostname.setter
    def hostname(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this instance was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def capacity_adjustment(self):
        """Capacity adjustment (float)"""
        return self._data.get("capacity_adjustment")

    @capacity_adjustment.setter
    def capacity_adjustment(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "capacity_adjustment", value, types.BOOLEAN, allowed_values)

    @property
    def version(self):
        """Version"""
        return self._data.get("version")

    @version.setter
    def version(self, value):
        raise ValueReadOnly

    @property
    def capacity(self):
        """Capacity (integer)"""
        return self._data.get("capacity")

    @capacity.setter
    def capacity(self, value):
        raise ValueReadOnly

    @property
    def consumed_capacity(self):
        """Consumed capacity (field)"""
        return self._data.get("consumed_capacity")

    @consumed_capacity.setter
    def consumed_capacity(self, value):
        raise ValueReadOnly

    @property
    def percent_capacity_remaining(self):
        """Percent capacity remaining (field)"""
        return self._data.get("percent_capacity_remaining")

    @percent_capacity_remaining.setter
    def percent_capacity_remaining(self, value):
        raise ValueReadOnly

    @property
    def jobs_running(self):
        """Count of jobs in the running or waiting state that are targeted for this instance (integer)"""
        return self._data.get("jobs_running")

    @jobs_running.setter
    def jobs_running(self, value):
        raise ValueReadOnly

    @property
    def jobs_total(self):
        """Count of all jobs that target this instance (integer)"""
        return self._data.get("jobs_total")

    @jobs_total.setter
    def jobs_total(self, value):
        raise ValueReadOnly

    @property
    def cpu(self):
        """Cpu (integer)"""
        return self._data.get("cpu")

    @cpu.setter
    def cpu(self, value):
        raise ValueReadOnly

    @property
    def memory(self):
        """Memory (integer)"""
        return self._data.get("memory")

    @memory.setter
    def memory(self, value):
        raise ValueReadOnly

    @property
    def cpu_capacity(self):
        """Cpu capacity (integer)"""
        return self._data.get("cpu_capacity")

    @cpu_capacity.setter
    def cpu_capacity(self, value):
        raise ValueReadOnly

    @property
    def mem_capacity(self):
        """Memory capacity (integer)"""
        return self._data.get("mem_capacity")

    @mem_capacity.setter
    def mem_capacity(self, value):
        raise ValueReadOnly

    @property
    def enabled(self):
        """Enabled (boolean)"""
        return self._data.get("enabled")

    @enabled.setter
    def enabled(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "enabled", value, types.BOOLEAN, allowed_values)

    @property
    def managed_by_policy(self):
        """Managed by policy (boolean)"""
        return self._data.get("managed_by_policy")

    @managed_by_policy.setter
    def managed_by_policy(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "managed_by_policy", value, types.BOOLEAN, allowed_values)
