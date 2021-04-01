from pyawx.models import types
from pyawx.models.mixins import DataModelMixin
from pyawx.models.utils import set_changes
from pyawx.exceptions import ValueReadOnly


class JobTemplate(DataModelMixin):
    __endpoint__ = "/api/v2/job_templates"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param name: Name of this job template.
            :type name: str, required
            :param description: Optional description of this job template.
            :type description: str, default ""
            :param job_type: Job type
            :type job_type: str, choice, Default run
                | run: Run
                | check: Check
            :param inventory: Inventory
            :type inventory: int, Default ``
            :param project: Project
            :type project: int, Default ``
            :param playbook: Playbook
            :type playbook: str, Default ""
            :param scm_branch: Branch to use in job run. Project default used if blank. Only allowed
                if project allow_override field is set to true. (string)
            :type scm_branch: str, Default ""
            :param forks: Forks
            :type forks: int, Default 0
            :param limit: Limit
            :type limit: str, Default ""
            :param verbosity: Verbosity
            :type verbosity: int, choice, Default 0
                | 0: 0 (Normal)
                | 1: 1 (Verbose)
                | 2: 2 (More Verbose)
                | 3: 3 (Debug)
                | 4: 4 (Connection Debug)
                | 5: 5 (WinRM Debug)
            :param extra_vars: Extra vars
            :type extra_vars: json, Default ``
            :param job_tags: Job tags
            :type job_tags: str, Default ""
            :param force_handlers: Force handler
            :type force_handlers: bool, Default False
            :param skip_tags: Skip tags
            :type skip_tags: str, Default ""
            :param start_at_task: Start at task
            :type start_at_task: str, Default ""
            :param timeout: The amount of time (in seconds) to run before the task is canceled.
            :type timeout: int, Default 0
            :param use_fact_cache: If enabled, Tower will act as an Ansible Fact Cache Plugin; persisting facts at
                the end of a playbook run to the database and caching facts for use by Ansible.
            :type use_fact_cache: bool, Default False
            :param host_config_key: host config key
            :type host_config_key: str, Default ""
            :param ask_scm_branch_on_launch: Ask SCM branch on launch
            :type ask_scm_branch_on_launch: bool, Default False
            :param ask_diff_mode_on_launch: Ask diff mode on launch
            :type ask_diff_mode_on_launch: bool, Default False
            :param ask_variables_on_launch: Ask variables on launch
            :type ask_variables_on_launch: bool, Default False
            :param ask_limit_on_launch: Ask limit on launch
            :type ask_limit_on_launch: bool, Default False
            :param ask_tags_on_launch: Ask tags on launch
            :type ask_tags_on_launch: bool, Default False
            :param ask_skip_tags_on_launch: Ask skip tags on launch
            :type ask_skip_tags_on_launch: bool, Default False
            :param ask_job_type_on_launch: Ask job type on launch
            :type ask_job_type_on_launch: bool, Default False
            :param ask_verbosity_on_launch: Ask verbosity on launch
            :type ask_verbosity_on_launch: bool, Default False
            :param ask_inventory_on_launch: Ask inventory on launch
            :type ask_inventory_on_launch: bool, Default False
            :param ask_credential_on_launch: Ask credential on launch
            :type ask_credential_on_launch: bool, Default False
            :param survey_enabled: Survey enabled
            :type survey_enabled: bool, Default False
            :param become_enabled: Become enabled
            :type become_enabled: bool, Default False
            :param diff_mode: If enabled, textual changes made to any templated files on the host are shown
                in the standard output
            :type diff_mode: bool, Default False
            :param allow_simultaneous: Allow simultaneous
            :type allow_simultaneous: bool, Default False
            :param custom_virtualenv: Local absolute file path containing a custom Python virtualenv to use (string)
            :type custom_virtualenv: str, Default ""
            :param job_slice_count: The number of jobs to slice into at runtime. Will cause the Job Template to
                launch a workflow if value is greater than 1.
            :type job_slice_count: int, Default 1
            :param webhook_service: Service that webhook requests will be accepted from.
            :type str, choice, Default ""
                | "": ---------
                | github: GitHub
                | gitlab: GitLab
            :param webhook_credential: Personal Access Token for posting back the status to the service API
            :type webhook_credential: int, Default ``


        Read Only Attributes:
            :param id: Database ID for this job template.
            :type id: int, readonly
            :param type: Data type for this job template.
            :type type: str, readonly
            :param url: URL for this job template.
            :type url: str, readonly
            :param created: Timestamp when this job template was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this job template was last modified.
            :type modified: datetime, readonly
            :param organization: The organization used to determine access to this template.
            :type organization: int, readonly
            :param last_job_run: Last job run
            :type last_job_run: datetime, readonly
            :param last_job_failed: Last job failed
            :type last_job_failed: bool, readonly
            :param next_job_run: Next job run
            :type next_job_run: datetime, readonly
            :param status: Status
            :type status: str, readonly
                | new: New
                | pending: Pending
                | waiting: Waiting
                | running: Running
                | successful: Successful
                | failed: Failed
                | error: Error
                | canceled: Canceled
                | never updated: Never Updated
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this job template. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this job template. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this job template. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this job template was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this job template was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this job template. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this job template. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def job_type(self):
        """Optional job_type of this job template. (string)"""
        return self._data.get("job_type")

    @job_type.setter
    def job_type(self, value):
        allowed_values = [
            "run",
            "check"
        ]
        set_changes(self, "job_type", value, types.STRING, allowed_values)

    @property
    def inventory(self):
        """Inventory (id)"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        set_changes(self, "inventory", value, types.INTEGER)

    @property
    def project(self):
        """Project (id)"""
        return self._data.get("project")

    @project.setter
    def project(self, value):
        set_changes(self, "project", value, types.INTEGER)

    @property
    def playbook(self):
        """Playbook (string)"""
        return self._data.get("playbook")

    @playbook.setter
    def playbook(self, value):
        set_changes(self, "playbook", value, types.STRING)

    @property
    def scm_branch(self):
        """
        Branch to use in job run. Project default used if blank. Only allowed if project allow_override
        field is set to true. (string)
        """
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
        set_changes(self, "scm_branch", value, types.STRING)

    @property
    def forks(self):
        """Forks (integer)"""
        return self._data.get("forks")

    @forks.setter
    def forks(self, value):
        set_changes(self, "forks", value, types.INTEGER)

    @property
    def limit(self):
        """Limit (string)"""
        return self._data.get("limit")

    @limit.setter
    def limit(self, value):
        set_changes(self, "limit", value, types.STRING)

    @property
    def verbosity(self):
        """Verbosity (int)"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        allowed_values = [
            0,
            1,
            2,
            3,
            4,
            5
        ]
        set_changes(self, "verbosity", value, types.INTEGER, allowed_values)

    @property
    def extra_vars(self):
        """Extra vars (json)"""
        return self._data.get("extra_vars")

    @extra_vars.setter
    def extra_vars(self, value):
        set_changes(self, "extra_vars", value, types.JSON)

    @property
    def job_tags(self):
        """Job tags (string)"""
        return self._data.get("job_tags")

    @job_tags.setter
    def job_tags(self, value):
        set_changes(self, "job_tags", value, types.STRING)

    @property
    def force_handlers(self):
        """Force handlers (boolean)"""
        return self._data.get("force_handlers")

    @force_handlers.setter
    def force_handlers(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "force_handlers", value, types.BOOLEAN, allowed_values)

    @property
    def skip_tags(self):
        """Skip tags (string)"""
        return self._data.get("skip_tags")

    @skip_tags.setter
    def skip_tags(self, value):
        set_changes(self, "skip_tags", value, types.STRING)

    @property
    def start_at_task(self):
        """Start at task (string)"""
        return self._data.get("start_at_task")

    @start_at_task.setter
    def start_at_task(self, value):
        set_changes(self, "start_at_task", value, types.STRING)

    @property
    def timeout(self):
        """The amount of time (in seconds) to run before the task is canceled. (integer)"""
        return self._data.get("timeout")

    @timeout.setter
    def timeout(self, value):
        set_changes(self, "timeout", value, types.INTEGER)

    @property
    def use_fact_cache(self):
        """
        If enabled, Tower will act as an Ansible Fact Cache Plugin; persisting facts at the end of a
        playbook run to the database and caching facts for use by Ansible. (boolean)
        """
        return self._data.get("use_fact_cache")

    @use_fact_cache.setter
    def use_fact_cache(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "use_fact_cache", value, types.BOOLEAN, allowed_values)

    @property
    def organization(self):
        """The organization used to determine access to this template. (id)"""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        raise ValueReadOnly

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
        """Last job failed"""
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
    def host_config_key(self):
        """Host config key"""
        return self._data.get("host_config_key")

    @host_config_key.setter
    def host_config_key(self, value):
        set_changes(self, "host_config_key", value, types.STRING)

    @property
    def ask_scm_branch_on_launch(self):
        """Ask SCAM branch on launch (boolean)"""
        return self._data.get("ask_scm_branch_on_launch")

    @ask_scm_branch_on_launch.setter
    def ask_scm_branch_on_launch(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "ask_scm_branch_on_launch", value, types.BOOLEAN, allowed_values)

    @property
    def ask_diff_mode_on_launch(self):
        """Ask diff mode on launch (boolean)"""
        return self._data.get("ask_diff_mode_on_launch")

    @ask_diff_mode_on_launch.setter
    def ask_diff_mode_on_launch(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "ask_diff_mode_on_launch", value, types.BOOLEAN, allowed_values)

    @property
    def ask_variables_on_launch(self):
        """Ask variables on launch (boolean)"""
        return self._data.get("ask_variables_on_launch")

    @ask_variables_on_launch.setter
    def ask_variables_on_launch(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "ask_variables_on_launch", value, types.BOOLEAN, allowed_values)

    @property
    def ask_limit_on_launch(self):
        """Ask limit on launch (boolean)"""
        return self._data.get("ask_limit_on_launch")

    @ask_limit_on_launch.setter
    def ask_limit_on_launch(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "ask_limit_on_launch", value, types.BOOLEAN, allowed_values)

    @property
    def ask_tags_on_launch(self):
        """Ask tags on launch (boolean)"""
        return self._data.get("ask_tags_on_launch")

    @ask_tags_on_launch.setter
    def ask_tags_on_launch(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "ask_tags_on_launch", value, types.BOOLEAN, allowed_values)

    @property
    def ask_skip_tags_on_launch(self):
        """Ask skip tags on launch (boolean)"""
        return self._data.get("ask_skip_tags_on_launch")

    @ask_skip_tags_on_launch.setter
    def ask_skip_tags_on_launch(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "ask_skip_tags_on_launch", value, types.BOOLEAN, allowed_values)

    @property
    def ask_job_type_on_launch(self):
        """Ask job type on launch (boolean)"""
        return self._data.get("ask_job_type_on_launch")

    @ask_job_type_on_launch.setter
    def ask_job_type_on_launch(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "ask_job_type_on_launch", value, types.BOOLEAN, allowed_values)

    @property
    def ask_verbosity_on_launch(self):
        """Ask verbosity on launch (boolean)"""
        return self._data.get("ask_verbosity_on_launch")

    @ask_verbosity_on_launch.setter
    def ask_verbosity_on_launch(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "ask_verbosity_on_launch", value, types.BOOLEAN, allowed_values)

    @property
    def ask_inventory_on_launch(self):
        """Ask inventory on launch (boolean)"""
        return self._data.get("ask_inventory_on_launch")

    @ask_inventory_on_launch.setter
    def ask_inventory_on_launch(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "ask_inventory_on_launch", value, types.BOOLEAN, allowed_values)

    @property
    def ask_credential_on_launch(self):
        """Ask credentials on launch (boolean)"""
        return self._data.get("ask_credential_on_launch")

    @ask_credential_on_launch.setter
    def ask_credential_on_launch(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "ask_credential_on_launch", value, types.BOOLEAN, allowed_values)

    @property
    def survey_enabled(self):
        """Survey enabled (boolean)"""
        return self._data.get("survey_enabled")

    @survey_enabled.setter
    def survey_enabled(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "survey_enabled", value, types.BOOLEAN, allowed_values)

    @property
    def become_enabled(self):
        """Become enabled (boolean)"""
        return self._data.get("become_enabled")

    @become_enabled.setter
    def become_enabled(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "become_enabled", value, types.BOOLEAN, allowed_values)

    @property
    def diff_mode(self):
        """
        If enabled, textual changes made to any templated files on the host are shown in
        the standard output (boolean)
        """
        return self._data.get("diff_mode")

    @diff_mode.setter
    def diff_mode(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "diff_mode", value, types.BOOLEAN, allowed_values)

    @property
    def allow_simultaneous(self):
        """Allow simultaneous (boolean)"""
        return self._data.get("allow_simultaneous")

    @allow_simultaneous.setter
    def allow_simultaneous(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "allow_simultaneous", value, types.BOOLEAN, allowed_values)

    @property
    def custom_virtualenv(self):
        """Local absolute file path containing a custom Python virtualenv to use (string)"""
        return self._data.get("custom_virtualenv")

    @custom_virtualenv.setter
    def custom_virtualenv(self, value):
        set_changes(self, "custom_virtualenv", value, types.STRING)

    @property
    def job_slice_count(self):
        """
        The number of jobs to slice into at runtime. Will cause the Job Template to launch a workflow
        if value is greater than 1. (integer)
        """
        return self._data.get("job_slice_count")

    @job_slice_count.setter
    def job_slice_count(self, value):
        set_changes(self, "job_slice_count", value, types.INTEGER)

    @property
    def webhook_service(self):
        """Service that webhook requests will be accepted from (choice)"""
        return self._data.get("webhook_service")

    @webhook_service.setter
    def webhook_service(self, value):
        allowed_values = [
            "",
            "github",
            "gitlab"
        ]
        set_changes(self, "webhook_service", value, types.STRING, allowed_values)

    @property
    def webhook_credential(self):
        """Personal Access Token for posting back the status to the service API (id)"""
        return self._data.get("webhook_credential")

    @webhook_credential.setter
    def webhook_credential(self, value):
        set_changes(self, "webhook_credential", value, types.INTEGER)


class Job(DataModelMixin):
    __endpoint__ = "/api/v2/job_templates"

    def __init__(self, **kwargs):
        """
         Read Only Attributes:
            :param id: Database ID for this job.
            :type id: int, readonly
            :param type: Data type for this job.
            :type type: str, readonly
            :param url: URL for this job.
            :type url: str, readonly
            :param created: Timestamp when this job was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this job was last modified.
            :type modified: datetime, readonly
            :param name: Name of this job.
            :type name: str, readonly
            :param description: Optional description of this job. (string)
            :type description: str, readonly
            :param unified_job_template: Unified job template
            :type unified_job_template: int, readonly
            :param launch_type: Launch type
            :type launch_type: str, readonly
                | manual: Manual
                | relaunch: Relaunch
                | callback: Callback
                | scheduled: Scheduled
                | dependency: Dependency
                | workflow: Workflow
                | webhook: Webhook
                | sync: Sync
                | scm: SCM Update
            :param status: Status
            :type status: str, readonly
                | new: New
                | pending: Pending
                | waiting: Waiting
                | running: Running
                | successful: Successful
                | failed: Failed
                | error: Error
                | canceled: Canceled
            :param failed: Failed
            :type failed: bool, readonly
            :param started: The date and time the job was queued for starting.
            :type started: datetime, readonly
            :param finished: The date and time the job finished execution.
            :type finished: datetime, readonly
            :param canceled_on: The date and time when the cancel request was sent.
            :type canceled_on: datetime, readonly
            :param elapsed: Elapsed time in seconds that the job ran.
            :type elapsed: float, readonly
            :param job_explanation: A status field to indicate the state of the job if it
                wasn’t able to run and capture stdout.
            :type job_explanation: str, readonly
            :param execution_node: The node the job executed on.
            :type execution_node: str, readonly
            :param controller_node: The instance that managed the isolated execution environment.
            :type controller_node: str, readonly
            :param job_type: Job type
            :type job_type: str, readonly
                | run: Run
                | check: Check
                | scan: Scan
            :param inventory: Inventory
            :type inventory: id, readonly
            :param project: Project
            :type project: int, readonly
            :param playbook: Playbook
            :type playbook: str, readonly
            :param scm_branch: Branch to use in job run. Project default used if blank. Only allowed if
                project allow_override field is set to true.
            :type scm_branch: str, readonly
            :param forks: Forks
            :type forks: int, readonly
            :param limit: Limit
            :type limit: str, readonly
            :param verbosity: Verbosity
            :type verbosity: int, readonly
                | 0: 0 (Normal)
                | 1: 1 (Verbose)
                | 2: 2 (More Verbose)
                | 3: 3 (Debug)
                | 4: 4 (Connection Debug)
                | 5: 5 (WinRM Debug)
            :param extra_vars: Extra vars
            :type extra_vars:: json, readonly
            :param job_tags: Job tags
            :type job_tags: str, readonly
            :param force_handlers: Force handlers
            :type force_handlers: bool, readonly
            :param skip_tags: Skip tags
            :type skip_tags: str, readonly
            :param start_at_task: Start at task
            :type start_at_task: str, readonly
            :param timeout: The amount of time (in seconds) to run before the task is canceled.
            :type timeout: int, readonly
            :param use_fact_cache: If enabled, Tower will act as an Ansible Fact Cache Plugin; persisting
                facts at the end of a playbook run to the database and caching facts for use by Ansible.
            :type use_fact_cache: bool, readonly
            :param organization: The organization used to determine access to this unified job.
            :type organization: int, readonly
            :param job_template: Job template
            :type job_template: int, readonly
            :param passwords_needed_to_start: Passwords needed to start
            :type passwords_needed_to_start: str, readonly
            :param allow_simultaneous: Allow simultaneous
            :type allow_simultaneous: bool, readonly
            :param artifacts: Artifacts
            :type artifacts: json, readonly
            :param scm_revision: The SCM Revision from the Project used for this job, if available
            :type scm_revision: str, readonly
            :param instance_group: The Instance group the job was run under
            :type instance_group: int, readonly
            :param diff_mode: If enabled, textual changes made to any templated files on the host
                are shown in the standard output
            :type diff_mode: bool, readonly
            :param job_slice_number: If part of a sliced job, the ID of the inventory slice operated on.
                If not part of sliced job, parameter is not used.
            :type job_slice_number: int, readonly
            :param job_slice_count: If ran as part of sliced jobs, the total number of slices.
                If 1, job is not part of a sliced job.
            :type job_slice_count: int, readonly
            :param webhook_service: Service that webhook requests will be accepted from
            :type webhook_service: str, readonly
                | "": ---------
                | github: GitHub
                | gitlab: GitLab
            :param webhook_credential: Personal Access Token for posting back the status to the service API
            :type webhook_credential: id, readonly
            :param webhook_guid: Unique identifier of the event that triggered this webhook
            :type webhook_guid: str, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this job. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this job. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this job. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this job was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this job was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this job. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this job. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        raise ValueReadOnly

    @property
    def unified_job_template(self):
        """Unified job template (id)"""
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
        """Status (choice)"""
        return self._data.get("status")

    @status.setter
    def status(self, value):
        raise ValueReadOnly

    @property
    def failed(self):
        """Failed (boolean)"""
        return self._data.get("failed")

    @failed.setter
    def failed(self, value):
        raise ValueReadOnly

    @property
    def started(self):
        """The date and time the job was queued for starting. (datetime)"""
        return self._data.get("started")

    @started.setter
    def started(self, value):
        raise ValueReadOnly

    @property
    def finished(self):
        """The date and time the job finished execution. (datetime)"""
        return self._data.get("finished")

    @finished.setter
    def finished(self, value):
        raise ValueReadOnly

    @property
    def canceled_on(self):
        """The date and time when the cancel request was sent. (datetime)"""
        return self._data.get("canceled_on")

    @canceled_on.setter
    def canceled_on(self, value):
        raise ValueReadOnly

    @property
    def elapsed(self):
        """Elapsed time in seconds that the job ran. (decimal)"""
        return self._data.get("elapsed")

    @elapsed.setter
    def elapsed(self, value):
        raise ValueReadOnly

    @property
    def job_explanation(self):
        """A status field to indicate the state of the job if it wasn’t able to run and capture stdout (string)"""
        return self._data.get("job_explanation")

    @job_explanation.setter
    def job_explanation(self, value):
        raise ValueReadOnly

    @property
    def execution_node(self):
        """The node the job executed on. (string)"""
        return self._data.get("execution_node")

    @execution_node.setter
    def execution_node(self, value):
        raise ValueReadOnly

    @property
    def controller_node(self):
        """The instance that managed the isolated execution environment. (string)"""
        return self._data.get("controller_node")

    @controller_node.setter
    def controller_node(self, value):
        raise ValueReadOnly

    @property
    def job_type(self):
        """Job type (choice)"""
        return self._data.get("job_type")

    @job_type.setter
    def job_type(self, value):
        raise ValueReadOnly

    @property
    def inventory(self):
        """Inventory (id)"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        raise ValueReadOnly

    @property
    def project(self):
        """Project (id)"""
        return self._data.get("project")

    @project.setter
    def project(self, value):
        raise ValueReadOnly

    @property
    def playbook(self):
        """Playbook (string)"""
        return self._data.get("playbook")

    @playbook.setter
    def playbook(self, value):
        raise ValueReadOnly

    @property
    def scm_branch(self):
        """
        Branch to use in job run. Project default used if blank. Only allowed
        if project allow_override field is set to true. (string)
        """
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
        raise ValueReadOnly

    @property
    def forks(self):
        """Forks (id)"""
        return self._data.get("forks")

    @forks.setter
    def forks(self, value):
        raise ValueReadOnly

    @property
    def limit(self):
        """Limit (id)"""
        return self._data.get("limit")

    @limit.setter
    def limit(self, value):
        raise ValueReadOnly

    @property
    def verbosity(self):
        """Verbosity (choice)"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        raise ValueReadOnly

    @property
    def extra_vars(self):
        """Extra vars (json)"""
        return self._data.get("extra_vars")

    @extra_vars.setter
    def extra_vars(self, value):
        raise ValueReadOnly

    @property
    def job_tags(self):
        """Job tags (json)"""
        return self._data.get("job_tags")

    @job_tags.setter
    def job_tags(self, value):
        raise ValueReadOnly

    @property
    def force_handlers(self):
        """Force handlers (boolean)"""
        return self._data.get("force_handlers")

    @force_handlers.setter
    def force_handlers(self, value):
        raise ValueReadOnly

    @property
    def skip_tags(self):
        """Skip tags (string)"""
        return self._data.get("skip_tags")

    @skip_tags.setter
    def skip_tags(self, value):
        raise ValueReadOnly

    @property
    def start_at_task(self):
        """Start at task (string)"""
        return self._data.get("start_at_task")

    @start_at_task.setter
    def start_at_task(self, value):
        raise ValueReadOnly

    @property
    def timeout(self):
        """The amount of time (in seconds) to run before the task is canceled. (integer)"""
        return self._data.get("timeout")

    @timeout.setter
    def timeout(self, value):
        raise ValueReadOnly

    @property
    def use_fact_cache(self):
        """
        If enabled, Tower will act as an Ansible Fact Cache Plugin; persisting facts at the end of a
        playbook run to the database and caching facts for use by Ansible. (boolean)
        """
        return self._data.get("use_fact_cache")

    @use_fact_cache.setter
    def use_fact_cache(self, value):
        raise ValueReadOnly

    @property
    def organization(self):
        """The organization used to determine access to this unified job. (id)"""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        raise ValueReadOnly

    @property
    def job_template(self):
        """Job template (id)"""
        return self._data.get("job_template")

    @job_template.setter
    def job_template(self, value):
        raise ValueReadOnly

    @property
    def passwords_needed_to_start(self):
        """Passwords needed to start (field)"""
        return self._data.get("passwords_needed_to_start")

    @passwords_needed_to_start.setter
    def passwords_needed_to_start(self, value):
        raise ValueReadOnly

    @property
    def allow_simultaneous(self):
        """Allow simultaneous (boolean)"""
        return self._data.get("allow_simultaneous")

    @allow_simultaneous.setter
    def allow_simultaneous(self, value):
        raise ValueReadOnly

    @property
    def artifacts(self):
        """Artifacts (json)"""
        return self._data.get("artifacts")

    @artifacts.setter
    def artifacts(self, value):
        raise ValueReadOnly

    @property
    def scm_revision(self):
        """The SCM Revision from the Project used for this job, if available (string)"""
        return self._data.get("scm_revision")

    @scm_revision.setter
    def scm_revision(self, value):
        raise ValueReadOnly

    @property
    def instance_group(self):
        """The Instance group the job was run under (id)"""
        return self._data.get("instance_group")

    @instance_group.setter
    def instance_group(self, value):
        raise ValueReadOnly

    @property
    def diff_mode(self):
        """
        If enabled, textual changes made to any templated files on the
        host are shown in the standard output (boolean)
        """
        return self._data.get("diff_mode")

    @diff_mode.setter
    def diff_mode(self, value):
        raise ValueReadOnly

    @property
    def job_slice_number(self):
        """
        If part of a sliced job, the ID of the inventory slice operated on.
        If not part of sliced job, parameter is not used. (integer)
        """
        return self._data.get("job_slice_number")

    @job_slice_number.setter
    def job_slice_number(self, value):
        raise ValueReadOnly

    @property
    def job_slice_count(self):
        """
        If ran as part of sliced jobs, the total number of slices.
        If 1, job is not part of a sliced job. (integer)
        """
        return self._data.get("job_slice_count")

    @job_slice_count.setter
    def job_slice_count(self, value):
        raise ValueReadOnly

    @property
    def webhook_service(self):
        """Service that webhook requests will be accepted from (choice)"""
        return self._data.get("webhook_service")

    @webhook_service.setter
    def webhook_service(self, value):
        raise ValueReadOnly

    @property
    def webhook_credential(self):
        """Personal Access Token for posting back the status to the service API (id)"""
        return self._data.get("webhook_credential")

    @webhook_credential.setter
    def webhook_credential(self, value):
        raise ValueReadOnly

    @property
    def webhook_guid(self):
        """Unique identifier of the event that triggered this webhook (string)"""
        return self._data.get("webhook_guid")

    @webhook_guid.setter
    def webhook_guid(self, value):
        raise ValueReadOnly


class JobEvent(DataModelMixin):
    __endpoint__ = "/api/v2/job_events"

    def __init__(self, **kwargs):
        """
        Read Only Attributes:
            :param id: Database ID for this job event.
            :type id: int, readonly
            :param type: Data type for this job event
            :type type: str, readonly
            :param url: URL for this job event.
            :type url: str, readonly
            :param created: Timestamp when this job event was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this job event was last modified.
            :type modified: datetime, readonly
            :param job: Job
            :type job: id, readonly
            :param event: Event
            :type event: str, readonly
                | runner_on_failed: Host Failed
                | runner_on_start: Host Started
                | runner_on_ok: Host OK
                | runner_on_error: Host Failure
                | runner_on_skipped: Host Skipped
                | runner_on_unreachable: Host Unreachable
                | runner_on_no_hosts: No Hosts Remaining
                | runner_on_async_poll: Host Polling
                | runner_on_async_ok: Host Async OK
                | runner_on_async_failed: Host Async Failure
                | runner_item_on_ok: Item OK
                | runner_item_on_failed: Item Failed
                | runner_item_on_skipped: Item Skipped
                | runner_retry: Host Retry
                | runner_on_file_diff: File Difference
                | playbook_on_start: Playbook Started
                | playbook_on_notify: Running Handlers
                | playbook_on_include: Including File
                | playbook_on_no_hosts_matched: No Hosts Matched
                | playbook_on_no_hosts_remaining: No Hosts Remaining
                | playbook_on_task_start: Task Started
                | playbook_on_vars_prompt: Variables Prompted
                | playbook_on_setup: Gathering Facts
                | playbook_on_import_for_host: internal: on Import for Host
                | playbook_on_not_import_for_host: internal: on Not Import for Host
                | playbook_on_play_start: Play Started
                | playbook_on_stats: Playbook Complete
                | debug: Debug
                | verbose: Verbose
                | deprecated: Deprecated
                | warning: Warning
                | system_warning: System Warning
                | error: Error
            :param counter: Counter
            :type counter: int, readonly
            :param event_display: Event display
            :type event_display: str, readonly
            :param event_data: Event data
            :type event_data: json, readonly
            :param event_level: Event level
            :type event_level: int, readonly
            :param failed: Failed
            :type failed: bool, readonly
            :param changed: Changed
            :type changed: bool, readonly
            :param uuid: UUID
            :type uuid: str, readonly
            :param parent_uuid: Parent UUID
            :type parent_uuid: str, readonly
            :param host: Host
            :type host: int, readonly
            :param host_name: Host name
            :type host_name: str, readonly
            :param playbook: Playbook
            :type playbook: str, readonly
            :param play: Play
            :type play: str, readonly
            :param task: Task
            :type task: str, readonly
            :param role: Role
            :type role: str, readonly
            :param stdout: stdout
            :type stdout: str, readonly
            :param start_line: Start line
            :type start_line: int, readonly
            :param end_line: End line
            :type end_line: id, readonly
            :param verbosity: Verbosity
            :type verbosity: int, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this job event. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this job event. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this job event. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this job event was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this job event was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def job(self):
        """Job (id)"""
        return self._data.get("job")

    @job.setter
    def job(self, value):
        raise ValueReadOnly

    @property
    def event(self):
        """Event (choice)"""
        return self._data.get("event")

    @event.setter
    def event(self, value):
        raise ValueReadOnly

    @property
    def counter(self):
        """Counter (int)"""
        return self._data.get("counter")

    @counter.setter
    def counter(self, value):
        raise ValueReadOnly

    @property
    def event_display(self):
        """Event display (string)"""
        return self._data.get("event_display")

    @event_display.setter
    def event_display(self, value):
        raise ValueReadOnly

    @property
    def event_data(self):
        """Event data (json)"""
        return self._data.get("event_data")

    @event_data.setter
    def event_data(self, value):
        raise ValueReadOnly

    @property
    def event_level(self):
        """Event level (int)"""
        return self._data.get("event_level")

    @event_level.setter
    def event_level(self, value):
        raise ValueReadOnly

    @property
    def failed(self):
        """Failed (boolean)"""
        return self._data.get("failed")

    @failed.setter
    def failed(self, value):
        raise ValueReadOnly

    @property
    def changed(self):
        """Changed (boolean)"""
        return self._data.get("changed")

    @changed.setter
    def changed(self, value):
        raise ValueReadOnly

    @property
    def uuid(self):
        """UUID (string)"""
        return self._data.get("uuid")

    @uuid.setter
    def uuid(self, value):
        raise ValueReadOnly

    @property
    def parent_uuid(self):
        """Parent UUID (string)"""
        return self._data.get("parent_uuid")

    @parent_uuid.setter
    def parent_uuid(self, value):
        raise ValueReadOnly

    @property
    def host(self):
        """Host (id)"""
        return self._data.get("host")

    @host.setter
    def host(self, value):
        raise ValueReadOnly

    @property
    def host_name(self):
        """Host name (string)"""
        return self._data.get("host_name")

    @host_name.setter
    def host_name(self, value):
        raise ValueReadOnly

    @property
    def playbook(self):
        """Playbook (string)"""
        return self._data.get("playbook")

    @playbook.setter
    def playbook(self, value):
        raise ValueReadOnly

    @property
    def play(self):
        """Play (string)"""
        return self._data.get("play")

    @play.setter
    def play(self, value):
        raise ValueReadOnly

    @property
    def task(self):
        """Task (string)"""
        return self._data.get("task")

    @task.setter
    def task(self, value):
        raise ValueReadOnly

    @property
    def role(self):
        """Role (string)"""
        return self._data.get("role")

    @role.setter
    def role(self, value):
        raise ValueReadOnly

    @property
    def stdout(self):
        """stdout (string)"""
        return self._data.get("stdout")

    @stdout.setter
    def stdout(self, value):
        raise ValueReadOnly

    @property
    def start_line(self):
        """Start line (integer)"""
        return self._data.get("start_line")

    @start_line.setter
    def start_line(self, value):
        raise ValueReadOnly

    @property
    def end_line(self):
        """End line (integer)"""
        return self._data.get("end_line")

    @end_line.setter
    def end_line(self, value):
        raise ValueReadOnly

    @property
    def verbosity(self):
        """Verbosity (integer)"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        raise ValueReadOnly


class JobHostSummary(DataModelMixin):
    __endpoint__ = "/api/v2/job_host_summaries"

    def __init__(self, **kwargs):
        """
        Read Only Attributes:
            :param id: Database ID for this job host summary.
            :type id: int, readonly
            :param type: Data type for this job host summary.
            :type type: str, readonly
            :param url: URL for this job event.
            :type url: str, readonly
            :param created: Timestamp when this job host summary was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this job host summary was last modified.
            :type modified: datetime, readonly
            :param job: Job
            :type job: int, readonly
            :param host: Host
            :type host: int, readonly
            :param host_name: Hostname
            :type host_name: str, readonly
            :param changed: Changed
            :type changed: int, readonly
            :param dark: Dark
            :type dark: int, readonly
            :param failures: Failures
            :type failures: int, readonly
            :param ok: Ok
            :type ok: int, readonly
            :param processed: Processed
            :type processed: int, readonly
            :param skipped: Skipped
            :type skipped: int, readonly
            :param failed: Failed
            :type failed: (boolean), readonly
            :param ignored: Ignored
            :type ignored: int, readonly
            :param rescued: Rescued
            :type rescued: int, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this job host summary. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this job host summary. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this job host summary. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this job host summary was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this job host summary was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def job(self):
        """Job (id)"""
        return self._data.get("job")

    @job.setter
    def job(self, value):
        raise ValueReadOnly

    @property
    def host(self):
        """Host (id)"""
        return self._data.get("host")

    @host.setter
    def host(self, value):
        raise ValueReadOnly

    @property
    def host_name(self):
        """Host name (string)"""
        return self._data.get("host_name")

    @host_name.setter
    def host_name(self, value):
        raise ValueReadOnly

    @property
    def changed(self):
        """Changed (integer)"""
        return self._data.get("changed")

    @changed.setter
    def changed(self, value):
        raise ValueReadOnly

    @property
    def dark(self):
        """Dark (integer)"""
        return self._data.get("dark")

    @dark.setter
    def dark(self, value):
        raise ValueReadOnly

    @property
    def failures(self):
        """Failures (integer)"""
        return self._data.get("failures")

    @failures.setter
    def failures(self, value):
        raise ValueReadOnly

    @property
    def ok(self):
        """Ok (integer)"""
        return self._data.get("ok")

    @ok.setter
    def ok(self, value):
        raise ValueReadOnly

    @property
    def processed(self):
        """Processed (integer)"""
        return self._data.get("processed")

    @processed.setter
    def processed(self, value):
        raise ValueReadOnly

    @property
    def skipped(self):
        """Skipped (integer)"""
        return self._data.get("skipped")

    @skipped.setter
    def skipped(self, value):
        raise ValueReadOnly

    @property
    def failed(self):
        """Failed (boolean)"""
        return self._data.get("failed")

    @failed.setter
    def failed(self, value):
        raise ValueReadOnly

    @property
    def ignored(self):
        """Ignored (integer)"""
        return self._data.get("ignored")

    @ignored.setter
    def ignored(self, value):
        raise ValueReadOnly

    @property
    def rescued(self):
        """Rescued (integer)"""
        return self._data.get("rescued")

    @rescued.setter
    def rescued(self, value):
        raise ValueReadOnly
