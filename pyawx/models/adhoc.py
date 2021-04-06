from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class AdHocCommand(DataModelMixin):
    __endpoint__ = "/api/v2/ad_hoc_commands"

    def __init__(self, **kwargs):
        """
        Ad Hoc Command List

        Attributes:
            :param job_type: Job type
                | run: Run
                | check: Check
            :type job_type: choice, required, default "run"
            :param inventory: Inventory
            :type inventory: id, required, default ``
            :param limit: Limit
            :type limit: string, required, default ""
            :param credential: Credential
            :type credential: id, required, default ``
            :param module_name: Module name
                | command: command
                | shell: shell
                | yum: yum
                | apt: apt
                | apt_key: apt_key
                | apt_repository: apt_repository
                | apt_rpm: apt_rpm
                | service: service
                | group: group
                | user: user
                | mount: mount
                | ping: ping
                | selinux: selinux
                | setup: setup
                | win_ping: win_ping
                | win_service: win_service
                | win_updates: win_updates
                | win_group: win_group
                | win_user: win_user
            :type module_name: choice, required, default "command"
            :param module_args: Module args
            :type module_args: string, required, default ""
            :param forks: Forks
            :type forks: integer, required, default 0
            :param verbosity: Verbosity
                | 0: 0 (Normal)
                | 1: 1 (Verbose)
                | 2: 2 (More Verbose)
                | 3: 3 (Debug)
                | 4: 4 (Connection Debug)
                | 5: 5 (WinRM Debug)
            :type verbosity: choice, required, default 0
            :param extra_vars: Extra vars
            :type extra_vars: string, required, default ""
            :param become_enabled: Become enabled
            :type become_enabled: boolean, required, default False
            :param diff_mode: Diff mode
            :type diff_mode: boolean, required, default False

        Read Only Attributes:
            :param id: Database ID for this ad hoc command.
            :type id: integer, readonly
            :param type: Data type for this ad hoc command.
                | ad_hoc_command: Command
            :type type: choice, readonly
            :param url: URL for this ad hoc command.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this ad hoc command was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this ad hoc command was last modified.
            :type modified: datetime, readonly
            :param name: Name of this ad hoc command.
            :type name: string, readonly
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
            :param controller_node: The instance that managed the isolated execution 
                environment.
            :type controller_node: string, readonly
            :param job_args: Job args
            :type job_args: string, readonly
            :param job_cwd: Job cwd
            :type job_cwd: string, readonly
            :param job_env: Job env
            :type job_env: json, readonly
            :param result_traceback: Result traceback
            :type result_traceback: string, readonly
            :param event_processing_finished: Indicates whether all of the events generated by this 
                unified job have been saved to the database.
            :type event_processing_finished: boolean, readonly
            :param host_status_counts: A count of hosts uniquely assigned to each status.
            :type host_status_counts: field, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this ad hoc command."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this ad hoc command."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this ad hoc command."""
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
        """Timestamp when this ad hoc command was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this ad hoc command was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this ad hoc command."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
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
    def controller_node(self):
        """The instance that managed the isolated execution environment."""
        return self._data.get("controller_node")

    @controller_node.setter
    def controller_node(self, value):
        raise ValueReadOnly

    @property
    def job_type(self):
        """Job type"""
        return self._data.get("job_type")

    @job_type.setter
    def job_type(self, value):
        allowed_values = [
            "run",
            "check"
        ]
        set_changes(self, "job_type", value, types.CHOICE, allowed_values)

    @property
    def inventory(self):
        """Inventory"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        set_changes(self, "inventory", value, types.ID)

    @property
    def limit(self):
        """Limit"""
        return self._data.get("limit")

    @limit.setter
    def limit(self, value):
        set_changes(self, "limit", value, types.STRING)

    @property
    def credential(self):
        """Credential"""
        return self._data.get("credential")

    @credential.setter
    def credential(self, value):
        set_changes(self, "credential", value, types.ID)

    @property
    def module_name(self):
        """Module name"""
        return self._data.get("module_name")

    @module_name.setter
    def module_name(self, value):
        allowed_values = [
            "command",
            "shell",
            "yum",
            "apt",
            "apt_key",
            "apt_repository",
            "apt_rpm",
            "service",
            "group",
            "user",
            "mount",
            "ping",
            "selinux",
            "setup",
            "win_ping",
            "win_service",
            "win_updates",
            "win_group",
            "win_user"
        ]
        set_changes(self, "module_name", value, types.CHOICE, allowed_values)

    @property
    def module_args(self):
        """Module args"""
        return self._data.get("module_args")

    @module_args.setter
    def module_args(self, value):
        set_changes(self, "module_args", value, types.STRING)

    @property
    def forks(self):
        """Forks"""
        return self._data.get("forks")

    @forks.setter
    def forks(self, value):
        set_changes(self, "forks", value, types.INTEGER)

    @property
    def verbosity(self):
        """Verbosity"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        allowed_values = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5"
        ]
        set_changes(self, "verbosity", value, types.CHOICE, allowed_values)

    @property
    def extra_vars(self):
        """Extra vars"""
        return self._data.get("extra_vars")

    @extra_vars.setter
    def extra_vars(self, value):
        set_changes(self, "extra_vars", value, types.STRING)

    @property
    def become_enabled(self):
        """Become enabled"""
        return self._data.get("become_enabled")

    @become_enabled.setter
    def become_enabled(self, value):
        set_changes(self, "become_enabled", value, types.BOOLEAN)

    @property
    def diff_mode(self):
        """Diff mode"""
        return self._data.get("diff_mode")

    @diff_mode.setter
    def diff_mode(self, value):
        set_changes(self, "diff_mode", value, types.BOOLEAN)

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
        """Job env"""
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
    def host_status_counts(self):
        """A count of hosts uniquely assigned to each status."""
        return self._data.get("host_status_counts")

    @host_status_counts.setter
    def host_status_counts(self, value):
        raise ValueReadOnly


class AdHocCommandEvent(DataModelMixin):
    __endpoint__ = "/api/v2/ad_hoc_command_events"

    def __init__(self, **kwargs):
        """
        Ad Hoc Command Event List

        Read Only Attributes:
            :param id: Database ID for this ad hoc command event.
            :type id: integer, readonly
            :param type: Data type for this ad hoc command event.
                | ad_hoc_command_event: Ad Hoc Command Event
            :type type: choice, readonly
            :param url: URL for this ad hoc command event.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this ad hoc command event was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this ad hoc command event was last modified.
            :type modified: datetime, readonly
            :param ad_hoc_command: Ad hoc command
            :type ad_hoc_command: id, readonly
            :param event: Event
                | runner_on_failed: Host Failed
                | runner_on_ok: Host OK
                | runner_on_unreachable: Host Unreachable
                | runner_on_skipped: Host Skipped
                | debug: Debug
                | verbose: Verbose
                | deprecated: Deprecated
                | warning: Warning
                | system_warning: System Warning
                | error: Error
            :type event: choice, readonly
            :param counter: Counter
            :type counter: integer, readonly
            :param event_display: Event display
            :type event_display: string, readonly
            :param event_data: Event data
            :type event_data: json, readonly
            :param failed: Failed
            :type failed: boolean, readonly
            :param changed: Changed
            :type changed: boolean, readonly
            :param uuid: Uuid
            :type uuid: string, readonly
            :param host: Host
            :type host: id, readonly
            :param host_name: Host name
            :type host_name: string, readonly
            :param stdout: Stdout
            :type stdout: string, readonly
            :param start_line: Start line
            :type start_line: integer, readonly
            :param end_line: End line
            :type end_line: integer, readonly
            :param verbosity: Verbosity
            :type verbosity: integer, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this ad hoc command event."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this ad hoc command event."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this ad hoc command event."""
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
        """Timestamp when this ad hoc command event was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this ad hoc command event was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def ad_hoc_command(self):
        """Ad hoc command"""
        return self._data.get("ad_hoc_command")

    @ad_hoc_command.setter
    def ad_hoc_command(self, value):
        raise ValueReadOnly

    @property
    def event(self):
        """Event"""
        return self._data.get("event")

    @event.setter
    def event(self, value):
        raise ValueReadOnly

    @property
    def counter(self):
        """Counter"""
        return self._data.get("counter")

    @counter.setter
    def counter(self, value):
        raise ValueReadOnly

    @property
    def event_display(self):
        """Event display"""
        return self._data.get("event_display")

    @event_display.setter
    def event_display(self, value):
        raise ValueReadOnly

    @property
    def event_data(self):
        """Event data"""
        return self._data.get("event_data")

    @event_data.setter
    def event_data(self, value):
        raise ValueReadOnly

    @property
    def failed(self):
        """Failed"""
        return self._data.get("failed")

    @failed.setter
    def failed(self, value):
        raise ValueReadOnly

    @property
    def changed(self):
        """Changed"""
        return self._data.get("changed")

    @changed.setter
    def changed(self, value):
        raise ValueReadOnly

    @property
    def uuid(self):
        """Uuid"""
        return self._data.get("uuid")

    @uuid.setter
    def uuid(self, value):
        raise ValueReadOnly

    @property
    def host(self):
        """Host"""
        return self._data.get("host")

    @host.setter
    def host(self, value):
        raise ValueReadOnly

    @property
    def host_name(self):
        """Host name"""
        return self._data.get("host_name")

    @host_name.setter
    def host_name(self, value):
        raise ValueReadOnly

    @property
    def stdout(self):
        """Stdout"""
        return self._data.get("stdout")

    @stdout.setter
    def stdout(self, value):
        raise ValueReadOnly

    @property
    def start_line(self):
        """Start line"""
        return self._data.get("start_line")

    @start_line.setter
    def start_line(self, value):
        raise ValueReadOnly

    @property
    def end_line(self):
        """End line"""
        return self._data.get("end_line")

    @end_line.setter
    def end_line(self, value):
        raise ValueReadOnly

    @property
    def verbosity(self):
        """Verbosity"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        raise ValueReadOnly
