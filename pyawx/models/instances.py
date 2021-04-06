from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class Instance(DataModelMixin):
    __endpoint__ = "/api/v2/instances"

    def __init__(self, **kwargs):
        """
        Instances

        Attributes:
            :param capacity_adjustment: Capacity adjustment
            :type capacity_adjustment: decimal, required, default "1.0"
            :param enabled: Enabled
            :type enabled: boolean, required, default True
            :param managed_by_policy: Managed by policy
            :type managed_by_policy: boolean, required, default True

        Read Only Attributes:
            :param id: Database ID for this instance.
            :type id: integer, readonly
            :param type: Data type for this instance.
                | instance: Instance
            :type type: choice, readonly
            :param url: URL for this instance.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param uuid: Uuid
            :type uuid: string, readonly
            :param hostname: Hostname
            :type hostname: string, readonly
            :param created: Timestamp when this instance was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this instance was last modified.
            :type modified: datetime, readonly
            :param version: Version
            :type version: string, readonly
            :param capacity: Capacity
            :type capacity: integer, readonly
            :param consumed_capacity: Consumed capacity
            :type consumed_capacity: field, readonly
            :param percent_capacity_remaining: Percent capacity remaining
            :type percent_capacity_remaining: field, readonly
            :param jobs_running: Count of jobs in the running or waiting state that are 
                targeted for this instance
            :type jobs_running: integer, readonly
            :param jobs_total: Count of all jobs that target this instance
            :type jobs_total: integer, readonly
            :param cpu: Cpu
            :type cpu: integer, readonly
            :param memory: Memory
            :type memory: integer, readonly
            :param cpu_capacity: Cpu capacity
            :type cpu_capacity: integer, readonly
            :param mem_capacity: Mem capacity
            :type mem_capacity: integer, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this instance."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this instance."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this instance."""
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
        """Timestamp when this instance was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this instance was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def capacity_adjustment(self):
        """Capacity adjustment"""
        return self._data.get("capacity_adjustment")

    @capacity_adjustment.setter
    def capacity_adjustment(self, value):
        set_changes(self, "capacity_adjustment", value, types.DECIMAL)

    @property
    def version(self):
        """Version"""
        return self._data.get("version")

    @version.setter
    def version(self, value):
        raise ValueReadOnly

    @property
    def capacity(self):
        """Capacity"""
        return self._data.get("capacity")

    @capacity.setter
    def capacity(self, value):
        raise ValueReadOnly

    @property
    def consumed_capacity(self):
        """Consumed capacity"""
        return self._data.get("consumed_capacity")

    @consumed_capacity.setter
    def consumed_capacity(self, value):
        raise ValueReadOnly

    @property
    def percent_capacity_remaining(self):
        """Percent capacity remaining"""
        return self._data.get("percent_capacity_remaining")

    @percent_capacity_remaining.setter
    def percent_capacity_remaining(self, value):
        raise ValueReadOnly

    @property
    def jobs_running(self):
        """Count of jobs in the running or waiting state that are targeted for this instance"""
        return self._data.get("jobs_running")

    @jobs_running.setter
    def jobs_running(self, value):
        raise ValueReadOnly

    @property
    def jobs_total(self):
        """Count of all jobs that target this instance"""
        return self._data.get("jobs_total")

    @jobs_total.setter
    def jobs_total(self, value):
        raise ValueReadOnly

    @property
    def cpu(self):
        """Cpu"""
        return self._data.get("cpu")

    @cpu.setter
    def cpu(self, value):
        raise ValueReadOnly

    @property
    def memory(self):
        """Memory"""
        return self._data.get("memory")

    @memory.setter
    def memory(self, value):
        raise ValueReadOnly

    @property
    def cpu_capacity(self):
        """Cpu capacity"""
        return self._data.get("cpu_capacity")

    @cpu_capacity.setter
    def cpu_capacity(self, value):
        raise ValueReadOnly

    @property
    def mem_capacity(self):
        """Mem capacity"""
        return self._data.get("mem_capacity")

    @mem_capacity.setter
    def mem_capacity(self, value):
        raise ValueReadOnly

    @property
    def enabled(self):
        """Enabled"""
        return self._data.get("enabled")

    @enabled.setter
    def enabled(self, value):
        set_changes(self, "enabled", value, types.BOOLEAN)

    @property
    def managed_by_policy(self):
        """Managed by policy"""
        return self._data.get("managed_by_policy")

    @managed_by_policy.setter
    def managed_by_policy(self, value):
        set_changes(self, "managed_by_policy", value, types.BOOLEAN)


class InstanceGroup(DataModelMixin):
    __endpoint__ = "/api/v2/instance_groups"

    def __init__(self, **kwargs):
        """
        Instance Groups

        Attributes:
            :param name: Name of this instance group.
            :type name: string, required, default ``
            :param credential: Credential
            :type credential: id, required, default ``
            :param policy_instance_percentage: Minimum percentage of all instances that will be 
                automatically assigned to this group when new instances
            :type policy_instance_percentage: integer, required, default 0
            :param policy_instance_minimum: Static minimum number of Instances that will be 
                automatically assign to this group when new instances come
            :type policy_instance_minimum: integer, required, default 0
            :param policy_instance_list: List of exact-match Instances that will be assigned to this 
                group
            :type policy_instance_list: json, required, default ``
            :param pod_spec_override: Pod spec override
            :type pod_spec_override: string, required, default "{'apiVersion': 'v1', 'kind': 'Pod', 'metadata': {'namespace': 'default'}, 'spec': {'containers': [{'image': 'ansible/ansible-runner', 'tty': True, 'stdin': True, 'imagePullPolicy': 'Always', 'args': ['sleep', 'infinity']}]}}"

        Read Only Attributes:
            :param id: Database ID for this instance group.
            :type id: integer, readonly
            :param type: Data type for this instance group.
                | instance_group: Instance Group
            :type type: choice, readonly
            :param url: URL for this instance group.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param created: Timestamp when this instance group was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this instance group was last modified.
            :type modified: datetime, readonly
            :param capacity: Capacity
            :type capacity: field, readonly
            :param committed_capacity: Committed capacity
            :type committed_capacity: field, readonly
            :param consumed_capacity: Consumed capacity
            :type consumed_capacity: field, readonly
            :param percent_capacity_remaining: Percent capacity remaining
            :type percent_capacity_remaining: field, readonly
            :param jobs_running: Count of jobs in the running or waiting state that are 
                targeted for this instance group
            :type jobs_running: integer, readonly
            :param jobs_total: Count of all jobs that target this instance group
            :type jobs_total: integer, readonly
            :param instances: Instances
            :type instances: field, readonly
            :param controller: Instance Group to remotely control this group.
            :type controller: id, readonly
            :param is_controller: Indicates whether instance group controls any other group
            :type is_controller: boolean, readonly
            :param is_isolated: Indicates whether instances in this group are 
                isolated.Isolated groups have a designated controller
            :type is_isolated: boolean, readonly
            :param is_containerized: Indicates whether instances in this group are 
                containerized.Containerized groups have a designated
            :type is_containerized: boolean, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this instance group."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this instance group."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this instance group."""
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
    def name(self):
        """Name of this instance group."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def created(self):
        """Timestamp when this instance group was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this instance group was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def capacity(self):
        """Capacity"""
        return self._data.get("capacity")

    @capacity.setter
    def capacity(self, value):
        raise ValueReadOnly

    @property
    def committed_capacity(self):
        """Committed capacity"""
        return self._data.get("committed_capacity")

    @committed_capacity.setter
    def committed_capacity(self, value):
        raise ValueReadOnly

    @property
    def consumed_capacity(self):
        """Consumed capacity"""
        return self._data.get("consumed_capacity")

    @consumed_capacity.setter
    def consumed_capacity(self, value):
        raise ValueReadOnly

    @property
    def percent_capacity_remaining(self):
        """Percent capacity remaining"""
        return self._data.get("percent_capacity_remaining")

    @percent_capacity_remaining.setter
    def percent_capacity_remaining(self, value):
        raise ValueReadOnly

    @property
    def jobs_running(self):
        """Count of jobs in the running or waiting state that are targeted for this instance group"""
        return self._data.get("jobs_running")

    @jobs_running.setter
    def jobs_running(self, value):
        raise ValueReadOnly

    @property
    def jobs_total(self):
        """Count of all jobs that target this instance group"""
        return self._data.get("jobs_total")

    @jobs_total.setter
    def jobs_total(self, value):
        raise ValueReadOnly

    @property
    def instances(self):
        """Instances"""
        return self._data.get("instances")

    @instances.setter
    def instances(self, value):
        raise ValueReadOnly

    @property
    def controller(self):
        """Instance Group to remotely control this group."""
        return self._data.get("controller")

    @controller.setter
    def controller(self, value):
        raise ValueReadOnly

    @property
    def is_controller(self):
        """Indicates whether instance group controls any other group"""
        return self._data.get("is_controller")

    @is_controller.setter
    def is_controller(self, value):
        raise ValueReadOnly

    @property
    def is_isolated(self):
        """Indicates whether instances in this group are isolated.Isolated groups have a designated controller 
        group."""
        return self._data.get("is_isolated")

    @is_isolated.setter
    def is_isolated(self, value):
        raise ValueReadOnly

    @property
    def is_containerized(self):
        """Indicates whether instances in this group are containerized.Containerized groups have a designated 
        Openshift or Kubernetes cluster."""
        return self._data.get("is_containerized")

    @is_containerized.setter
    def is_containerized(self, value):
        raise ValueReadOnly

    @property
    def credential(self):
        """Credential"""
        return self._data.get("credential")

    @credential.setter
    def credential(self, value):
        set_changes(self, "credential", value, types.ID)

    @property
    def policy_instance_percentage(self):
        """Minimum percentage of all instances that will be automatically assigned to this group when new instances 
        come online."""
        return self._data.get("policy_instance_percentage")

    @policy_instance_percentage.setter
    def policy_instance_percentage(self, value):
        set_changes(self, "policy_instance_percentage", value, types.INTEGER)

    @property
    def policy_instance_minimum(self):
        """Static minimum number of Instances that will be automatically assign to this group when new instances 
        come online."""
        return self._data.get("policy_instance_minimum")

    @policy_instance_minimum.setter
    def policy_instance_minimum(self, value):
        set_changes(self, "policy_instance_minimum", value, types.INTEGER)

    @property
    def policy_instance_list(self):
        """List of exact-match Instances that will be assigned to this group"""
        return self._data.get("policy_instance_list")

    @policy_instance_list.setter
    def policy_instance_list(self, value):
        set_changes(self, "policy_instance_list", value, types.JSON)

    @property
    def pod_spec_override(self):
        """Pod spec override"""
        return self._data.get("pod_spec_override")

    @pod_spec_override.setter
    def pod_spec_override(self, value):
        set_changes(self, "pod_spec_override", value, types.STRING)

    @property
    def summary_fields(self):
        """Data structure with name/description for related resources.  The output for some objects may be limited 
        for performance reasons."""
        return self._data.get("summary_fields")

    @summary_fields.setter
    def summary_fields(self, value):
        raise ValueReadOnly
