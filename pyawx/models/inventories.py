from pyawx.models import types
from pyawx.models.mixins import DataModelMixin
from pyawx.models.utils import set_changes
from pyawx.exceptions import ValueReadOnly


class Inventory(DataModelMixin):
    __endpoint__ = "/api/v2/inventories"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param name: Name of this inventory
            :type name: str, required
            :param description: Optional description of this inventory.
            :type description: str, default ""
            :param organization: Organization containing this application.
            :type organization: int, required
            :param kind: Kind of inventory being represented.
            :type kind: choice, str
                | "": Hosts have a direct link to this inventory.
                | smart: Hosts for inventory generated using the host_filter property.
            :param host_filter: Filter that will be applied to the hosts of this inventory.
            :type host_filter: str, Default ""
            :param variables: Inventory variables in JSON format.
            :type variables: json, Default ``
            :param insights_credential: Credentials to be used by hosts belonging to
                this inventory when accessing Red Hat Insights API.
            :type insights_credential: int, default ``

        Read Only Attributes:
            :param id: Database ID for this inventory.
            :type id: int, readonly
            :param type: Data type for this inventory.
            :type type: str, readonly
            :param url: URL for this inventory.
            :type url: str, readonly
            :param created: Timestamp when this inventory was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this inventory was last modified.
            :type modified: datetime, readonly
            :param has_active_failures: This field is deprecated and will be removed in a future release.
                Flag indicating whether any hosts in this inventory have failed.
            :type has_active_failures: bool, readonly
            :param total_hosts: This field is deprecated and will be removed in a future release.
                Total number of hosts in this inventory.
            :type total_hosts: int, readonly
            :param hosts_with_active_failures: This field is deprecated and will be removed in a future release.
                Number of hosts in this inventory with active failures.
            :type hosts_with_active_failures: int, readonly
            :param total_groups: This field is deprecated and will be removed in a future release.
                Total number of groups in this inventory.
            :type total_groups: int, readonly
            :param has_inventory_sources: This field is deprecated and will be removed in a future release.
                Flag indicating whether this inventory has any external inventory sources.
            :type has_inventory_sources: bool, readonly
            :param total_inventory_sources: Total number of external inventory sources configured within this inventory.
            :type total_inventory_sources: int, readonly
            :param inventory_sources_with_failures: Number of external inventory
                sources in this inventory with failures.
            :type inventory_sources_with_failures: int, readonly
            :param pending_deletion: Flag indicating the inventory is being deleted.
            :type pending_deletion: bool, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this inventory. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this inventory. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this inventory. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this inventory was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this inventory was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this inventory. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this inventory. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def organization(self):
        """Organization containing this application. (id)"""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.INTEGER)

    @property
    def kind(self):
        """Kind of inventory being represented. (choice)"""
        return self._data.get("kind")

    @kind.setter
    def kind(self, value):
        allowed_values = [
            "",
            "smart"
        ]
        set_changes(self, "kind", value, types.INTEGER, allowed_values)

    @property
    def host_filter(self):
        """Filter that will be applied to the hosts of this inventory. (string)"""
        return self._data.get("host_filter")

    @host_filter.setter
    def host_filter(self, value):
        set_changes(self, "host_filter", value, types.STRING)

    @property
    def variables(self):
        """Inventory variables in JSON format. (json)"""
        return self._data.get("variables")

    @variables.setter
    def variables(self, value):
        set_changes(self, "variables", value, types.JSON)

    @property
    def has_active_failures(self):
        """
        This field is deprecated and will be removed in a future release.
        Flag indicating whether any hosts in this inventory have failed. (boolean)
        """
        return self._data.get("has_active_failures")

    @has_active_failures.setter
    def has_active_failures(self, value):
        raise ValueReadOnly

    @property
    def total_hosts(self):
        """
        This field is deprecated and will be removed in a future release.
        Total number of hosts in this inventory. (integer)
        """
        return self._data.get("total_hosts")

    @total_hosts.setter
    def total_hosts(self, value):
        raise ValueReadOnly

    @property
    def hosts_with_active_failures(self):
        """
        This field is deprecated and will be removed in a future release.
        Number of hosts in this inventory with active failures. (integer)
        """
        return self._data.get("hosts_with_active_failures")

    @hosts_with_active_failures.setter
    def hosts_with_active_failures(self, value):
        raise ValueReadOnly

    @property
    def total_groups(self):
        """
        This field is deprecated and will be removed in a future release.
        Total number of groups in this inventory. (integer)
        """
        return self._data.get("total_groups")

    @total_groups.setter
    def total_groups(self, value):
        raise ValueReadOnly

    @property
    def has_inventory_sources(self):
        """
        This field is deprecated and will be removed in a future release.
        Flag indicating whether this inventory has any external inventory sources. (boolean)
        """
        return self._data.get("has_inventory_sources")

    @has_inventory_sources.setter
    def has_inventory_sources(self, value):
        raise ValueReadOnly

    @property
    def total_inventory_sources(self):
        """Total number of external inventory sources configured within this inventory. (integer)"""
        return self._data.get("total_inventory_sources")

    @total_inventory_sources.setter
    def total_inventory_sources(self, value):
        raise ValueReadOnly

    @property
    def inventory_sources_with_failures(self):
        """Number of external inventory sources in this inventory with failures. (integer)"""
        return self._data.get("inventory_sources_with_failures")

    @inventory_sources_with_failures.setter
    def inventory_sources_with_failures(self, value):
        raise ValueReadOnly

    @property
    def insights_credential(self):
        """Credentials to be used by hosts belonging to this inventory when accessing Red Hat Insights API. (id)"""
        return self._data.get("insights_credential")

    @insights_credential.setter
    def insights_credential(self, value):
        set_changes(self, "insights_credential", value, types.INTEGER)

    @property
    def pending_deletion(self):
        """Flag indicating the inventory is being deleted. (boolean)"""
        return self._data.get("pending_deletion")

    @pending_deletion.setter
    def pending_deletion(self, value):
        raise ValueReadOnly


class InventoryScript(DataModelMixin):
    __endpoint__ = "/api/v2/inventory_scripts"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param name: Name of this custom inventory script.
            :type name: str, required
            :param description: Optional description of this custom inventory script.
            :type description: str, default ""
            :param organization: Organization containing this application.
            :type organization: int, required
            :param script: Script
            :type script: str, required

        Read Only Attributes:
            :param id: Database ID for this custom inventory script.
            :type id: int, readonly
            :param type: Data type for this custom inventory script.
            :type type: str, readonly
            :param url: URL for this custom inventory script.
            :type url: str, readonly
            :param created: Timestamp when this custom inventory script was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this custom inventory script was last modified.
            :type modified: datetime, readonly

        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this custom inventory script. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this custom inventory script. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this custom inventory script. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this custom inventory script was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this custom inventory script was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this custom inventory script. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this custom inventory script. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def organization(self):
        """Organization owning this inventory script (id)"""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.INTEGER)

    @property
    def script(self):
        """Script (string)"""
        return self._data.get("script")

    @script.setter
    def script(self, value):
        set_changes(self, "script", value, types.STRING)


class InventorySource(DataModelMixin):
    __endpoint__ = "/api/v2/inventory_sources"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param name: Name of this custom inventory script.
            :type name: str, required
            :param description: Optional description of this custom inventory script.
            :type description: str, default ""
            :param source: Optional source of this custom inventory script.
            :type source: str, choice, required
                | file: File, Directory or Script
                | scm: Sourced from a Project
                | ec2: Amazon EC2
                | gce: Google Compute Engine
                | azure_rm: Microsoft Azure Resource Manager
                | vmware: VMware vCenter
                | satellite6: Red Hat Satellite 6
                | openstack: OpenStack
                | rhv: Red Hat Virtualization
                | tower: Ansible Tower
                | custom: Custom Script
            :param source_path: Source path
            :type source_path: str, default ""
            :param source_script: Source script
            :type source_script: int, default ``
            :param source_vars: Inventory source variables in JSON format.
            :type source_vars: str, default ""
            :param credential: Cloud credential to use for inventory updates.
            :type credential: int, default None
            :param enabled_var: Retrieve the enabled state from the given dict of host variables. The enabled
                variable may be specified as "foo.bar", in which case the lookup will traverse into nested dicts,
                equivalent to: from_dict.get("foo", {}).get("bar", default)
            :type enabled_var: str, default ""
            :param enabled_value: Only used when enabled_var is set. Value when the host is considered enabled.
                For example if enabled_var="status.power_state"and enabled_value="powered_on" with host
                variables:{ "status": { "power_state": "powered_on", "created": "2018-02-01T08:00:00.000000Z:00",
                "healthy": true }, "name": "foobar", "ip_address": "192.168.2.1"}The host would be marked enabled.
                If power_state where any value other than powered_on then the host would be disabled when imported
                into Tower. If the key is not found then the host will be enabled
            :type enabled_value: str, default ""
            :param host_filter: Regex where only matching hosts will be imported into Tower.
            :type host_filter: str, default ""
            :param overwrite: Overwrite local groups and hosts from remote inventory source.
            :type overwrite: bool, default False
            :param overwrite_vars: Overwrite local variables from remote inventory source.
            :type overwrite_vars: bool, default False
            :param custom_virtualenv: Local absolute file path containing a custom Python virtualenv to use
            :type custom_virtualenv: str, Default ""
            :param timeout: The amount of time (in seconds) to run before the task is canceled.
            :type timeout: int, Default 0
            :param verbosity: Verbosity
                | 0: 0 (WARNING)
                | 1: 1 (INFO)
                | 2: 2 (DEBUG)
            :type verbosity: int, choice, Default 1
            :param inventory: Inventory
            :type inventory: int, required
            :param update_on_launch: Update on launch
            :type update_on_launch: bool, Default False
            :param update_cache_timeout: Update Cache Timeout
            :type update_cache_timeout: int, Default 0
            :param source_project: Project containing inventory file used as source.
            :type source_project: int, Default ``
            :param update_on_project_update: Update on project update
            :type update_on_project_update: bool, Default False

        Read Only Attributes:
            :param id: Database ID for this inventory source.
            :type id: int, readonly
            :param type: Data type for this inventory source
            :type type: str, readonly
            :param url: URL for this inventory source.
            :type url: str, readonly
            :param created: Timestamp when this inventory source was created.
            :type created: datetime, readonly
            :param modified: Optional description of this inventory source.
            :type modified: datetime, readonly
            :param last_job_run: Last job run
            :type last_job_run: datetime, readonly
            :param last_job_failed: Last job failed
            :type last_jbo_failed: bool, readonly
            :param next_job_run: Next job run
            :type next_job_run: datetime, readonly
            :param status: Status
                | new: New
                | pending: Pending
                | waiting: Waiting
                | running: Running
                | successful: Successful
                | failed: Failed
                | error: Error
                | canceled: Canceled
                | never updated: Never Updated
                | none: No External Source
            :type status: str, choice, readonly
            :param last_update_failed: Last update failed
            :type last_update_failed: bool, readonly
            :param last_updated: Last updated
            :type last_updated: datetime, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this inventory source. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this inventory source. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this inventory source. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this inventory source was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this inventory source was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this inventory source. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this inventory source. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def source(self):
        """Optional source of this inventory source. (string)"""
        return self._data.get("source")

    @source.setter
    def source(self, value):
        allowed_values = [
            "file",
            "scm",
            "ec2",
            "gce",
            "azure_rm",
            "vmware",
            "satellite6",
            "openstack",
            "rhv",
            "tower",
            "custom"
        ]
        set_changes(self, "source", value, types.STRING, allowed_values)

    @property
    def source_path(self):
        """Source path"""
        return self._data.get("source_path")

    @source_path.setter
    def source_path(self, value):
        set_changes(self, "source_path", value, types.STRING)

    @property
    def source_script(self):
        """Source script"""
        return self._data.get("source_script")

    @source_script.setter
    def source_script(self, value):
        set_changes(self, "source_script", value, types.INTEGER)

    @property
    def source_vars(self):
        """Inventory source variables in JSON format. (string)"""
        return self._data.get("source_vars")

    @source_vars.setter
    def source_vars(self, value):
        set_changes(self, "source_vars", value, types.STRING)

    @property
    def credential(self):
        """Cloud credential to use for inventory updates. (integer)"""
        return self._data.get("credential")

    @credential.setter
    def credential(self, value):
        set_changes(self, "credential", value, types.INTEGER)

    @property
    def enabled_var(self):
        """
        Retrieve the enabled state from the given dict of host variables. The enabled variable may be
        specified as "foo.bar", in which case the lookup will traverse into nested dicts,
        equivalent to: from_dict.get("foo", {}).get("bar", default) (string)
        """
        return self._data.get("enabled_var")

    @enabled_var.setter
    def enabled_var(self, value):
        set_changes(self, "enabled_var", value, types.STRING)

    @property
    def enabled_value(self):
        """
        Only used when enabled_var is set. Value when the host is considered enabled. For example if
        enabled_var="status.power_state"and enabled_value="powered_on" with host
        variables:{ "status": { "power_state": "powered_on", "created": "2018-02-01T08:00:00.000000Z:00",
        "healthy": true }, "name": "foobar", "ip_address": "192.168.2.1"}The host would be marked enabled.
        If power_state where any value other than powered_on then the host would be disabled when imported into
        Tower. If the key is not found then the host will be enabled (string)
        """
        return self._data.get("enabled_value")

    @enabled_value.setter
    def enabled_value(self, value):
        set_changes(self, "enabled_value", value, types.STRING)

    @property
    def host_filter(self):
        """Regex where only matching hosts will be imported into Tower. (string)"""
        return self._data.get("host_filter")

    @host_filter.setter
    def host_filter(self, value):
        set_changes(self, "host_filter", value, types.STRING)

    @property
    def overwrite(self):
        """Overwrite local groups and hosts from remote inventory source. (boolean)"""
        return self._data.get("overwrite")

    @overwrite.setter
    def overwrite(self, value):
        set_changes(self, "overwrite", value, types.BOOLEAN)

    @property
    def overwrite_vars(self):
        """Overwrite local variables from remote inventory source. (boolean)"""
        return self._data.get("overwrite_vars")

    @overwrite_vars.setter
    def overwrite_vars(self, value):
        set_changes(self, "overwrite_vars", value, types.BOOLEAN)

    @property
    def custom_virtualenv(self):
        """Local absolute file path containing a custom Python virtualenv to use (string)"""
        return self._data.get("custom_virtualenv")

    @custom_virtualenv.setter
    def custom_virtualenv(self, value):
        set_changes(self, "custom_virtualenv", value, types.STRING)

    @property
    def timeout(self):
        """The amount of time (in seconds) to run before the task is canceled. (integer)"""
        return self._data.get("timeout")

    @timeout.setter
    def timeout(self, value):
        set_changes(self, "timeout", value, types.INTEGER)

    @property
    def verbosity(self):
        """Verbosity (integer)"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        allowed_values = [
            0,
            1,
            2
        ]
        set_changes(self, "verbosity", value, types.INTEGER, allowed_values)

    @property
    def last_job_run(self):
        """Last job run (datetime)"""
        return self._data.get("last_job_run")

    @last_job_run.setter
    def last_job_run(self, value):
        raise ValueReadOnly

    @property
    def last_job_failed(self):
        """Last job failed (boolean)"""
        return self._data.get("last_job_failed")

    @last_job_failed.setter
    def last_job_failed(self, value):
        raise ValueReadOnly

    @property
    def next_job_run(self):
        """next job run (datetime)"""
        return self._data.get("next_job_run")

    @next_job_run.setter
    def next_job_run(self, value):
        raise ValueReadOnly

    @property
    def status(self):
        """Status (choice)"""
        return self._data.get("status")

    @status.setter
    def status(self, value):
        raise ValueReadOnly

    @property
    def inventory(self):
        """Inventory (id)"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        set_changes(self, "inventory", value, types.INTEGER)

    @property
    def update_on_launch(self):
        """Update on launce (boolean)"""
        return self._data.get("update_on_launch")

    @update_on_launch.setter
    def update_on_launch(self, value):
        set_changes(self, "update_on_launch", value, types.BOOLEAN)

    @property
    def update_cache_timeout(self):
        """Update cache timeout (integer)"""
        return self._data.get("update_cache_timeout")

    @update_cache_timeout.setter
    def update_cache_timeout(self, value):
        set_changes(self, "update_cache_timeout", value, types.INTEGER)

    @property
    def source_project(self):
        """Project containing inventory file used as source. (id)"""
        return self._data.get("source_project")

    @source_project.setter
    def source_project(self, value):
        set_changes(self, "source_project", value, types.INTEGER)

    @property
    def update_on_project_update(self):
        """Update on project update (boolean)"""
        return self._data.get("update_on_project_update")

    @update_on_project_update.setter
    def update_on_project_update(self, value):
        set_changes(self, "update_on_project_update", value, types.BOOLEAN)

    @property
    def last_update_failed(self):
        """last update failed (boolean)"""
        return self._data.get("last_update_failed")

    @last_update_failed.setter
    def last_update_failed(self, value):
        raise ValueReadOnly

    @property
    def last_updated(self):
        """Last updated (datetime)"""
        return self._data.get("last_updated")

    @last_updated.setter
    def last_updated(self, value):
        raise ValueReadOnly
