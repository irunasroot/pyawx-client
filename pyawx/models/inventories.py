from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class Inventory(DataModelMixin):
    __endpoint__ = "/api/v2/inventories"

    def __init__(self, **kwargs):
        """
        Inventory List

        Attributes:
            :param name: Name of this inventory.
            :type name: string, required, default ``
            :param description: Optional description of this inventory.
            :type description: string, required, default ""
            :param organization: Organization containing this inventory.
            :type organization: id, required, default ``
            :param kind: Kind of inventory being represented.
                | : Hosts have a direct link to this inventory.
                | smart: Hosts for inventory generated using the host_filter property.
            :type kind: choice, required, default ""
            :param host_filter: Filter that will be applied to the hosts of this inventory.
            :type host_filter: string, required, default "None"
            :param variables: Inventory variables in JSON or YAML format.
            :type variables: json, required, default ""
            :param insights_credential: Credentials to be used by hosts belonging to this inventory 
                when accessing Red Hat Insights API.
            :type insights_credential: id, required, default ``

        Read Only Attributes:
            :param id: Database ID for this inventory.
            :type id: integer, readonly
            :param type: Data type for this inventory.
                | inventory: Inventory
            :type type: choice, readonly
            :param url: URL for this inventory.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this inventory was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this inventory was last modified.
            :type modified: datetime, readonly
            :param has_active_failures: This field is deprecated and will be removed in a future 
                release. Flag indicating whether any hosts in this
            :type has_active_failures: boolean, readonly
            :param total_hosts: This field is deprecated and will be removed in a future 
                release. Total number of hosts in this inventory.
            :type total_hosts: integer, readonly
            :param hosts_with_active_failures: This field is deprecated and will be removed in a future 
                release. Number of hosts in this inventory with active
            :type hosts_with_active_failures: integer, readonly
            :param total_groups: This field is deprecated and will be removed in a future 
                release. Total number of groups in this inventory.
            :type total_groups: integer, readonly
            :param has_inventory_sources: This field is deprecated and will be removed in a future 
                release. Flag indicating whether this inventory has any
            :type has_inventory_sources: boolean, readonly
            :param total_inventory_sources: Total number of external inventory sources configured 
                within this inventory.
            :type total_inventory_sources: integer, readonly
            :param inventory_sources_with_failures: Number of external inventory sources in this inventory with 
                failures.
            :type inventory_sources_with_failures: integer, readonly
            :param pending_deletion: Flag indicating the inventory is being deleted.
            :type pending_deletion: boolean, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this inventory."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this inventory."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this inventory."""
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
        """Timestamp when this inventory was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this inventory was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this inventory."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this inventory."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def organization(self):
        """Organization containing this inventory."""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.ID)

    @property
    def kind(self):
        """Kind of inventory being represented."""
        return self._data.get("kind")

    @kind.setter
    def kind(self, value):
        allowed_values = [
            "",
            "smart"
        ]
        set_changes(self, "kind", value, types.CHOICE, allowed_values)

    @property
    def host_filter(self):
        """Filter that will be applied to the hosts of this inventory."""
        return self._data.get("host_filter")

    @host_filter.setter
    def host_filter(self, value):
        set_changes(self, "host_filter", value, types.STRING)

    @property
    def variables(self):
        """Inventory variables in JSON or YAML format."""
        return self._data.get("variables")

    @variables.setter
    def variables(self, value):
        set_changes(self, "variables", value, types.JSON)

    @property
    def has_active_failures(self):
        """This field is deprecated and will be removed in a future release. Flag indicating whether any hosts in 
        this inventory have failed."""
        return self._data.get("has_active_failures")

    @has_active_failures.setter
    def has_active_failures(self, value):
        raise ValueReadOnly

    @property
    def total_hosts(self):
        """This field is deprecated and will be removed in a future release. Total number of hosts in this 
        inventory."""
        return self._data.get("total_hosts")

    @total_hosts.setter
    def total_hosts(self, value):
        raise ValueReadOnly

    @property
    def hosts_with_active_failures(self):
        """This field is deprecated and will be removed in a future release. Number of hosts in this inventory with 
        active failures."""
        return self._data.get("hosts_with_active_failures")

    @hosts_with_active_failures.setter
    def hosts_with_active_failures(self, value):
        raise ValueReadOnly

    @property
    def total_groups(self):
        """This field is deprecated and will be removed in a future release. Total number of groups in this 
        inventory."""
        return self._data.get("total_groups")

    @total_groups.setter
    def total_groups(self, value):
        raise ValueReadOnly

    @property
    def has_inventory_sources(self):
        """This field is deprecated and will be removed in a future release. Flag indicating whether this inventory 
        has any external inventory sources."""
        return self._data.get("has_inventory_sources")

    @has_inventory_sources.setter
    def has_inventory_sources(self, value):
        raise ValueReadOnly

    @property
    def total_inventory_sources(self):
        """Total number of external inventory sources configured within this inventory."""
        return self._data.get("total_inventory_sources")

    @total_inventory_sources.setter
    def total_inventory_sources(self, value):
        raise ValueReadOnly

    @property
    def inventory_sources_with_failures(self):
        """Number of external inventory sources in this inventory with failures."""
        return self._data.get("inventory_sources_with_failures")

    @inventory_sources_with_failures.setter
    def inventory_sources_with_failures(self, value):
        raise ValueReadOnly

    @property
    def insights_credential(self):
        """Credentials to be used by hosts belonging to this inventory when accessing Red Hat Insights API."""
        return self._data.get("insights_credential")

    @insights_credential.setter
    def insights_credential(self, value):
        set_changes(self, "insights_credential", value, types.ID)

    @property
    def pending_deletion(self):
        """Flag indicating the inventory is being deleted."""
        return self._data.get("pending_deletion")

    @pending_deletion.setter
    def pending_deletion(self, value):
        raise ValueReadOnly


class InventoryScript(DataModelMixin):
    __endpoint__ = "/api/v2/inventory_scripts"

    def __init__(self, **kwargs):
        """
        Inventory Script List

        Attributes:
            :param name: Name of this custom inventory script.
            :type name: string, required, default ``
            :param description: Optional description of this custom inventory script.
            :type description: string, required, default ""
            :param script: Script
            :type script: string, required, default ``
            :param organization: Organization owning this inventory script
            :type organization: id, required, default ``

        Read Only Attributes:
            :param id: Database ID for this custom inventory script.
            :type id: integer, readonly
            :param type: Data type for this custom inventory script.
                | custom_inventory_script: Custom Inventory Script
            :type type: choice, readonly
            :param url: URL for this custom inventory script.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this custom inventory script was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this custom inventory script was last 
                modified.
            :type modified: datetime, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this custom inventory script."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this custom inventory script."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this custom inventory script."""
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
        """Timestamp when this custom inventory script was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this custom inventory script was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this custom inventory script."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this custom inventory script."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def script(self):
        """Script"""
        return self._data.get("script")

    @script.setter
    def script(self, value):
        set_changes(self, "script", value, types.STRING)

    @property
    def organization(self):
        """Organization owning this inventory script"""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.ID)


class InventorySource(DataModelMixin):
    __endpoint__ = "/api/v2/inventory_sources"

    def __init__(self, **kwargs):
        """
        Inventory Source List

        Attributes:
            :param name: Name of this inventory source.
            :type name: string, required, default ``
            :param description: Optional description of this inventory source.
            :type description: string, required, default ""
            :param source: Source
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
            :type source: choice, required, default "None"
            :param source_path: Source path
            :type source_path: string, required, default ""
            :param source_script: Source script
            :type source_script: id, required, default ``
            :param source_vars: Inventory source variables in YAML or JSON format.
            :type source_vars: string, required, default ""
            :param credential: Cloud credential to use for inventory updates.
            :type credential: integer, required, default "None"
            :param enabled_var: Retrieve the enabled state from the given dict of host 
                variables. The enabled variable may be specified as 
                neste
            :type enabled_var: string, required, default ""
            :param enabled_value: Only used when enabled_var is set. Value when the host is 
                considered enabled. For example if 
                _o
            :type enabled_value: string, required, default ""
            :param host_filter: Regex where only matching hosts will be imported into 
                Tower.
            :type host_filter: string, required, default ""
            :param overwrite: Overwrite local groups and hosts from remote inventory 
                source.
            :type overwrite: boolean, required, default False
            :param overwrite_vars: Overwrite local variables from remote inventory source.
            :type overwrite_vars: boolean, required, default False
            :param custom_virtualenv: Local absolute file path containing a custom Python 
                virtualenv to use
            :type custom_virtualenv: string, required, default "None"
            :param timeout: The amount of time (in seconds) to run before the task is 
                canceled.
            :type timeout: integer, required, default 0
            :param verbosity: Verbosity
                | 0: 0 (WARNING)
                | 1: 1 (INFO)
                | 2: 2 (DEBUG)
            :type verbosity: choice, required, default 1
            :param inventory: Inventory
            :type inventory: id, required, default ``
            :param update_on_launch: Update on launch
            :type update_on_launch: boolean, required, default False
            :param update_cache_timeout: Update cache timeout
            :type update_cache_timeout: integer, required, default 0
            :param source_project: Project containing inventory file used as source.
            :type source_project: id, required, default ``
            :param update_on_project_update: Update on project update
            :type update_on_project_update: boolean, required, default False

        Read Only Attributes:
            :param id: Database ID for this inventory source.
            :type id: integer, readonly
            :param type: Data type for this inventory source.
                | inventory_source: Inventory Source
            :type type: choice, readonly
            :param url: URL for this inventory source.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this inventory source was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this inventory source was last modified.
            :type modified: datetime, readonly
            :param last_job_run: Last job run
            :type last_job_run: datetime, readonly
            :param last_job_failed: Last job failed
            :type last_job_failed: boolean, readonly
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
            :type status: choice, readonly
            :param last_update_failed: Last update failed
            :type last_update_failed: boolean, readonly
            :param last_updated: Last updated
            :type last_updated: datetime, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this inventory source."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this inventory source."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this inventory source."""
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
        """Timestamp when this inventory source was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this inventory source was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this inventory source."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this inventory source."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def source(self):
        """Source"""
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
        set_changes(self, "source", value, types.CHOICE, allowed_values)

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
        set_changes(self, "source_script", value, types.ID)

    @property
    def source_vars(self):
        """Inventory source variables in YAML or JSON format."""
        return self._data.get("source_vars")

    @source_vars.setter
    def source_vars(self, value):
        set_changes(self, "source_vars", value, types.STRING)

    @property
    def credential(self):
        """Cloud credential to use for inventory updates."""
        return self._data.get("credential")

    @credential.setter
    def credential(self, value):
        set_changes(self, "credential", value, types.INTEGER)

    @property
    def enabled_var(self):
        """Retrieve the enabled state from the given dict of host variables. The enabled variable may be specified 
        as "foo.bar", in which case the lookup will traverse into nested dicts, equivalent to: 
        """
        return self._data.get("enabled_var")

    @enabled_var.setter
    def enabled_var(self, value):
        set_changes(self, "enabled_var", value, types.STRING)

    @property
    def enabled_value(self):
        """Only used when enabled_var is set. Value when the host is considered enabled. For example if 
        enabled_var="status.power_state"and enabled_value="powered_on" with host variables:{   "status": {     
           },    
        """
        return self._data.get("enabled_value")

    @enabled_value.setter
    def enabled_value(self, value):
        set_changes(self, "enabled_value", value, types.STRING)

    @property
    def host_filter(self):
        """Regex where only matching hosts will be imported into Tower."""
        return self._data.get("host_filter")

    @host_filter.setter
    def host_filter(self, value):
        set_changes(self, "host_filter", value, types.STRING)

    @property
    def overwrite(self):
        """Overwrite local groups and hosts from remote inventory source."""
        return self._data.get("overwrite")

    @overwrite.setter
    def overwrite(self, value):
        set_changes(self, "overwrite", value, types.BOOLEAN)

    @property
    def overwrite_vars(self):
        """Overwrite local variables from remote inventory source."""
        return self._data.get("overwrite_vars")

    @overwrite_vars.setter
    def overwrite_vars(self, value):
        set_changes(self, "overwrite_vars", value, types.BOOLEAN)

    @property
    def custom_virtualenv(self):
        """Local absolute file path containing a custom Python virtualenv to use"""
        return self._data.get("custom_virtualenv")

    @custom_virtualenv.setter
    def custom_virtualenv(self, value):
        set_changes(self, "custom_virtualenv", value, types.STRING)

    @property
    def timeout(self):
        """The amount of time (in seconds) to run before the task is canceled."""
        return self._data.get("timeout")

    @timeout.setter
    def timeout(self, value):
        set_changes(self, "timeout", value, types.INTEGER)

    @property
    def verbosity(self):
        """Verbosity"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        allowed_values = [
            "0",
            "1",
            "2"
        ]
        set_changes(self, "verbosity", value, types.CHOICE, allowed_values)

    @property
    def last_job_run(self):
        """Last job run"""
        return self._data.get("last_job_run")

    @last_job_run.setter
    def last_job_run(self, value):
        raise ValueReadOnly

    @property
    def last_job_failed(self):
        """Last job failed"""
        return self._data.get("last_job_failed")

    @last_job_failed.setter
    def last_job_failed(self, value):
        raise ValueReadOnly

    @property
    def next_job_run(self):
        """Next job run"""
        return self._data.get("next_job_run")

    @next_job_run.setter
    def next_job_run(self, value):
        raise ValueReadOnly

    @property
    def status(self):
        """Status"""
        return self._data.get("status")

    @status.setter
    def status(self, value):
        raise ValueReadOnly

    @property
    def inventory(self):
        """Inventory"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        set_changes(self, "inventory", value, types.ID)

    @property
    def update_on_launch(self):
        """Update on launch"""
        return self._data.get("update_on_launch")

    @update_on_launch.setter
    def update_on_launch(self, value):
        set_changes(self, "update_on_launch", value, types.BOOLEAN)

    @property
    def update_cache_timeout(self):
        """Update cache timeout"""
        return self._data.get("update_cache_timeout")

    @update_cache_timeout.setter
    def update_cache_timeout(self, value):
        set_changes(self, "update_cache_timeout", value, types.INTEGER)

    @property
    def source_project(self):
        """Project containing inventory file used as source."""
        return self._data.get("source_project")

    @source_project.setter
    def source_project(self, value):
        set_changes(self, "source_project", value, types.ID)

    @property
    def update_on_project_update(self):
        """Update on project update"""
        return self._data.get("update_on_project_update")

    @update_on_project_update.setter
    def update_on_project_update(self, value):
        set_changes(self, "update_on_project_update", value, types.BOOLEAN)

    @property
    def last_update_failed(self):
        """Last update failed"""
        return self._data.get("last_update_failed")

    @last_update_failed.setter
    def last_update_failed(self, value):
        raise ValueReadOnly

    @property
    def last_updated(self):
        """Last updated"""
        return self._data.get("last_updated")

    @last_updated.setter
    def last_updated(self, value):
        raise ValueReadOnly


class InventoryUpdate(DataModelMixin):
    __endpoint__ = "/api/v2/inventory_updates"

    def __init__(self, **kwargs):
        """
        Inventory Update List

        Read Only Attributes:
            :param id: Database ID for this inventory update.
            :type id: integer, readonly
            :param type: Data type for this inventory update.
                | inventory_update: Inventory Sync
            :type type: choice, readonly
            :param url: URL for this inventory update.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this inventory update was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this inventory update was last modified.
            :type modified: datetime, readonly
            :param name: Name of this inventory update.
            :type name: string, readonly
            :param description: Optional description of this inventory update.
            :type description: string, readonly
            :param unified_job_template: unified job template
            :type unified_job_template: id, readonly
            :param launch_type: Launch type
                | manual: Manual
                | relaunch: Relaunch
                | callback: Callback
                | scheduled: Scheduled
                | dependency: Dependency
                | workflow: Workflow
                | webhook: Webhook
                | sync: Sync
                | scm: SCM Update
            :type launch_type: choice, readonly
            :param status: Status
                | new: New
                | pending: Pending
                | waiting: Waiting
                | running: Running
                | successful: Successful
                | failed: Failed
                | error: Error
                | canceled: Canceled
            :type status: choice, readonly
            :param failed: Failed
            :type failed: boolean, readonly
            :param started: The date and time the job was queued for starting.
            :type started: datetime, readonly
            :param finished: The date and time the job finished execution.
            :type finished: datetime, readonly
            :param canceled_on: The date and time when the cancel request was sent.
            :type canceled_on: datetime, readonly
            :param elapsed: Elapsed time in seconds that the job ran.
            :type elapsed: decimal, readonly
            :param job_explanation: A status field to indicate the state of the job if it 
                wasn't able to run and capture stdout
            :type job_explanation: string, readonly
            :param execution_node: The node the job executed on.
            :type execution_node: string, readonly
            :param source: Source
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
            :type source: choice, readonly
            :param source_path: Source path
            :type source_path: string, readonly
            :param source_script: Source script
            :type source_script: id, readonly
            :param source_vars: Inventory source variables in YAML or JSON format.
            :type source_vars: string, readonly
            :param credential: Cloud credential to use for inventory updates.
            :type credential: integer, readonly
            :param enabled_var: Retrieve the enabled state from the given dict of host 
                variables. The enabled variable may be specified as 
                neste
            :type enabled_var: string, readonly
            :param enabled_value: Only used when enabled_var is set. Value when the host is 
                considered enabled. For example if 
                _o
            :type enabled_value: string, readonly
            :param host_filter: Regex where only matching hosts will be imported into 
                Tower.
            :type host_filter: string, readonly
            :param overwrite: Overwrite local groups and hosts from remote inventory 
                source.
            :type overwrite: boolean, readonly
            :param overwrite_vars: Overwrite local variables from remote inventory source.
            :type overwrite_vars: boolean, readonly
            :param custom_virtualenv: Custom virtualenv
            :type custom_virtualenv: string, readonly
            :param timeout: The amount of time (in seconds) to run before the task is 
                canceled.
            :type timeout: integer, readonly
            :param verbosity: Verbosity
                | 0: 0 (WARNING)
                | 1: 1 (INFO)
                | 2: 2 (DEBUG)
            :type verbosity: choice, readonly
            :param inventory: Inventory
            :type inventory: id, readonly
            :param inventory_source: Inventory source
            :type inventory_source: id, readonly
            :param license_error: License error
            :type license_error: boolean, readonly
            :param org_host_limit_error: Org host limit error
            :type org_host_limit_error: boolean, readonly
            :param source_project_update: Inventory files from this Project Update were used for the 
                inventory update.
            :type source_project_update: id, readonly
            :param job_args: Job args
            :type job_args: string, readonly
            :param job_cwd: Job cwd
            :type job_cwd: string, readonly
            :param job_env: job_env
            :type job_env: json, readonly
            :param result_traceback: Result traceback
            :type result_traceback: string, readonly
            :param event_processing_finished: Indicates whether all of the events generated by this 
                unified job have been saved to the database.
            :type event_processing_finished: boolean, readonly
            :param source_project: The project used for this job.
            :type source_project: field, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this inventory update."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this inventory update."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this inventory update."""
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
        """Timestamp when this inventory update was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this inventory update was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this inventory update."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this inventory update."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        raise ValueReadOnly

    @property
    def unified_job_template(self):
        """unified job template"""
        return self._data.get("unified_job_template")

    @unified_job_template.setter
    def unified_job_template(self, value):
        raise ValueReadOnly

    @property
    def launch_type(self):
        """Launch type"""
        return self._data.get("launch_type")

    @launch_type.setter
    def launch_type(self, value):
        raise ValueReadOnly

    @property
    def status(self):
        """Status"""
        return self._data.get("status")

    @status.setter
    def status(self, value):
        raise ValueReadOnly

    @property
    def failed(self):
        """Failed"""
        return self._data.get("failed")

    @failed.setter
    def failed(self, value):
        raise ValueReadOnly

    @property
    def started(self):
        """The date and time the job was queued for starting."""
        return self._data.get("started")

    @started.setter
    def started(self, value):
        raise ValueReadOnly

    @property
    def finished(self):
        """The date and time the job finished execution."""
        return self._data.get("finished")

    @finished.setter
    def finished(self, value):
        raise ValueReadOnly

    @property
    def canceled_on(self):
        """The date and time when the cancel request was sent."""
        return self._data.get("canceled_on")

    @canceled_on.setter
    def canceled_on(self, value):
        raise ValueReadOnly

    @property
    def elapsed(self):
        """Elapsed time in seconds that the job ran."""
        return self._data.get("elapsed")

    @elapsed.setter
    def elapsed(self, value):
        raise ValueReadOnly

    @property
    def job_explanation(self):
        """A status field to indicate the state of the job if it wasn't able to run and capture stdout"""
        return self._data.get("job_explanation")

    @job_explanation.setter
    def job_explanation(self, value):
        raise ValueReadOnly

    @property
    def execution_node(self):
        """The node the job executed on."""
        return self._data.get("execution_node")

    @execution_node.setter
    def execution_node(self, value):
        raise ValueReadOnly

    @property
    def source(self):
        """Source"""
        return self._data.get("source")

    @source.setter
    def source(self, value):
        raise ValueReadOnly

    @property
    def source_path(self):
        """Source path"""
        return self._data.get("source_path")

    @source_path.setter
    def source_path(self, value):
        raise ValueReadOnly

    @property
    def source_script(self):
        """Source script"""
        return self._data.get("source_script")

    @source_script.setter
    def source_script(self, value):
        raise ValueReadOnly

    @property
    def source_vars(self):
        """Inventory source variables in YAML or JSON format."""
        return self._data.get("source_vars")

    @source_vars.setter
    def source_vars(self, value):
        raise ValueReadOnly

    @property
    def credential(self):
        """Cloud credential to use for inventory updates."""
        return self._data.get("credential")

    @credential.setter
    def credential(self, value):
        raise ValueReadOnly

    @property
    def enabled_var(self):
        """Retrieve the enabled state from the given dict of host variables. The enabled variable may be specified 
        as "foo.bar", in which case the lookup will traverse into nested dicts, equivalent to: 
        """
        return self._data.get("enabled_var")

    @enabled_var.setter
    def enabled_var(self, value):
        raise ValueReadOnly

    @property
    def enabled_value(self):
        """Only used when enabled_var is set. Value when the host is considered enabled. For example if 
        enabled_var="status.power_state"and enabled_value="powered_on" with host variables:{   "status": {     
           },    
        """
        return self._data.get("enabled_value")

    @enabled_value.setter
    def enabled_value(self, value):
        raise ValueReadOnly

    @property
    def host_filter(self):
        """Regex where only matching hosts will be imported into Tower."""
        return self._data.get("host_filter")

    @host_filter.setter
    def host_filter(self, value):
        raise ValueReadOnly

    @property
    def overwrite(self):
        """Overwrite local groups and hosts from remote inventory source."""
        return self._data.get("overwrite")

    @overwrite.setter
    def overwrite(self, value):
        raise ValueReadOnly

    @property
    def overwrite_vars(self):
        """Overwrite local variables from remote inventory source."""
        return self._data.get("overwrite_vars")

    @overwrite_vars.setter
    def overwrite_vars(self, value):
        raise ValueReadOnly

    @property
    def custom_virtualenv(self):
        """Custom virtualenv"""
        return self._data.get("custom_virtualenv")

    @custom_virtualenv.setter
    def custom_virtualenv(self, value):
        raise ValueReadOnly

    @property
    def timeout(self):
        """The amount of time (in seconds) to run before the task is canceled."""
        return self._data.get("timeout")

    @timeout.setter
    def timeout(self, value):
        raise ValueReadOnly

    @property
    def verbosity(self):
        """Verbosity"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        raise ValueReadOnly

    @property
    def inventory(self):
        """Inventory"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        raise ValueReadOnly

    @property
    def inventory_source(self):
        """Inventory source"""
        return self._data.get("inventory_source")

    @inventory_source.setter
    def inventory_source(self, value):
        raise ValueReadOnly

    @property
    def license_error(self):
        """License error"""
        return self._data.get("license_error")

    @license_error.setter
    def license_error(self, value):
        raise ValueReadOnly

    @property
    def org_host_limit_error(self):
        """Org host limit error"""
        return self._data.get("org_host_limit_error")

    @org_host_limit_error.setter
    def org_host_limit_error(self, value):
        raise ValueReadOnly

    @property
    def source_project_update(self):
        """Inventory files from this Project Update were used for the inventory update."""
        return self._data.get("source_project_update")

    @source_project_update.setter
    def source_project_update(self, value):
        raise ValueReadOnly

    @property
    def job_args(self):
        """Job args"""
        return self._data.get("job_args")

    @job_args.setter
    def job_args(self, value):
        raise ValueReadOnly

    @property
    def job_cwd(self):
        """Job cwd"""
        return self._data.get("job_cwd")

    @job_cwd.setter
    def job_cwd(self, value):
        raise ValueReadOnly

    @property
    def job_env(self):
        """job_env"""
        return self._data.get("job_env")

    @job_env.setter
    def job_env(self, value):
        raise ValueReadOnly

    @property
    def result_traceback(self):
        """Result traceback"""
        return self._data.get("result_traceback")

    @result_traceback.setter
    def result_traceback(self, value):
        raise ValueReadOnly

    @property
    def event_processing_finished(self):
        """Indicates whether all of the events generated by this unified job have been saved to the database."""
        return self._data.get("event_processing_finished")

    @event_processing_finished.setter
    def event_processing_finished(self, value):
        raise ValueReadOnly

    @property
    def source_project(self):
        """The project used for this job."""
        return self._data.get("source_project")

    @source_project.setter
    def source_project(self, value):
        raise ValueReadOnly


class Group(DataModelMixin):
    __endpoint__ = "/api/v2/groups"

    def __init__(self, **kwargs):
        """
        Group List

        Attributes:
            :param name: Name of this group.
            :type name: string, required, default ``
            :param description: Optional description of this group.
            :type description: string, required, default ""
            :param inventory: Inventory
            :type inventory: id, required, default ``
            :param variables: Group variables in JSON or YAML format.
            :type variables: json, required, default ""

        Read Only Attributes:
            :param id: Database ID for this group.
            :type id: integer, readonly
            :param type: Data type for this group.
                | group: Group
            :type type: choice, readonly
            :param url: URL for this group.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this group was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this group was last modified.
            :type modified: datetime, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this group."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this group."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this group."""
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
        """Timestamp when this group was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this group was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this group."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this group."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def inventory(self):
        """Inventory"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        set_changes(self, "inventory", value, types.ID)

    @property
    def variables(self):
        """Group variables in JSON or YAML format."""
        return self._data.get("variables")

    @variables.setter
    def variables(self, value):
        set_changes(self, "variables", value, types.JSON)


class Host(DataModelMixin):
    __endpoint__ = "/api/v2/hosts"

    def __init__(self, **kwargs):
        """
        Host List

        Attributes:
            :param name: Name of this host.
            :type name: string, required, default ``
            :param description: Optional description of this host.
            :type description: string, required, default ""
            :param inventory: Inventory
            :type inventory: id, required, default ``
            :param enabled: Is this host online and available for running jobs?
            :type enabled: boolean, required, default True
            :param instance_id: The value used by the remote inventory source to uniquely 
                identify the host
            :type instance_id: string, required, default ""
            :param variables: Host variables in JSON or YAML format.
            :type variables: json, required, default ""

        Read Only Attributes:
            :param id: Database ID for this host.
            :type id: integer, readonly
            :param type: Data type for this host.
                | host: Host
            :type type: choice, readonly
            :param url: URL for this host.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this host was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this host was last modified.
            :type modified: datetime, readonly
            :param has_active_failures: Has active failures
            :type has_active_failures: field, readonly
            :param has_inventory_sources: Has inventory sources
            :type has_inventory_sources: field, readonly
            :param last_job: Last job
            :type last_job: id, readonly
            :param last_job_host_summary: Last job host summary
            :type last_job_host_summary: id, readonly
            :param insights_system_id: Red Hat Insights host unique identifier.
            :type insights_system_id: string, readonly
            :param ansible_facts_modified: The date and time ansible_facts was last modified.
            :type ansible_facts_modified: datetime, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this host."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this host."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this host."""
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
        """Timestamp when this host was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this host was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this host."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this host."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def inventory(self):
        """Inventory"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        set_changes(self, "inventory", value, types.ID)

    @property
    def enabled(self):
        """Is this host online and available for running jobs?"""
        return self._data.get("enabled")

    @enabled.setter
    def enabled(self, value):
        set_changes(self, "enabled", value, types.BOOLEAN)

    @property
    def instance_id(self):
        """The value used by the remote inventory source to uniquely identify the host"""
        return self._data.get("instance_id")

    @instance_id.setter
    def instance_id(self, value):
        set_changes(self, "instance_id", value, types.STRING)

    @property
    def variables(self):
        """Host variables in JSON or YAML format."""
        return self._data.get("variables")

    @variables.setter
    def variables(self, value):
        set_changes(self, "variables", value, types.JSON)

    @property
    def has_active_failures(self):
        """Has active failures"""
        return self._data.get("has_active_failures")

    @has_active_failures.setter
    def has_active_failures(self, value):
        raise ValueReadOnly

    @property
    def has_inventory_sources(self):
        """Has inventory sources"""
        return self._data.get("has_inventory_sources")

    @has_inventory_sources.setter
    def has_inventory_sources(self, value):
        raise ValueReadOnly

    @property
    def last_job(self):
        """Last job"""
        return self._data.get("last_job")

    @last_job.setter
    def last_job(self, value):
        raise ValueReadOnly

    @property
    def last_job_host_summary(self):
        """Last job host summary"""
        return self._data.get("last_job_host_summary")

    @last_job_host_summary.setter
    def last_job_host_summary(self, value):
        raise ValueReadOnly

    @property
    def insights_system_id(self):
        """Red Hat Insights host unique identifier."""
        return self._data.get("insights_system_id")

    @insights_system_id.setter
    def insights_system_id(self, value):
        raise ValueReadOnly

    @property
    def ansible_facts_modified(self):
        """The date and time ansible_facts was last modified."""
        return self._data.get("ansible_facts_modified")

    @ansible_facts_modified.setter
    def ansible_facts_modified(self, value):
        raise ValueReadOnly
