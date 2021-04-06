from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class JobTemplate(DataModelMixin):
    __endpoint__ = "/api/v2/job_templates"

    def __init__(self, **kwargs):
        """
        Job Template List

        Attributes:
            :param name: Name of this job template.
            :type name: string, required, default ``
            :param description: Optional description of this job template.
            :type description: string, required, default ""
            :param job_type: Job type
                | run: Run
                | check: Check
            :type job_type: choice, required, default "run"
            :param inventory: Inventory
            :type inventory: id, required, default ``
            :param project: Project
            :type project: id, required, default ``
            :param playbook: Playbook
            :type playbook: string, required, default ""
            :param scm_branch: Branch to use in job run. Project default used if blank. 
                Only allowed if project allow_override field is set to
            :type scm_branch: string, required, default ""
            :param forks: Forks
            :type forks: integer, required, default 0
            :param limit: Limit
            :type limit: string, required, default ""
            :param verbosity: Verbosity
                | 0: 0 (Normal)
                | 1: 1 (Verbose)
                | 2: 2 (More Verbose)
                | 3: 3 (Debug)
                | 4: 4 (Connection Debug)
                | 5: 5 (WinRM Debug)
            :type verbosity: choice, required, default 0
            :param extra_vars: Extra vars
            :type extra_vars: json, required, default ""
            :param job_tags: Job tags
            :type job_tags: string, required, default ""
            :param force_handlers: Force handlers
            :type force_handlers: boolean, required, default False
            :param skip_tags: Skip tags
            :type skip_tags: string, required, default ""
            :param start_at_task: Start at task
            :type start_at_task: string, required, default ""
            :param timeout: The amount of time (in seconds) to run before the task is 
                canceled.
            :type timeout: integer, required, default 0
            :param use_fact_cache: If enabled, Tower will act as an Ansible Fact Cache Plugin; 
                persisting facts at the end of a playbook run to the
            :type use_fact_cache: boolean, required, default False
            :param host_config_key: Host config key
            :type host_config_key: string, required, default ""
            :param ask_scm_branch_on_launch: Ask scm branch on launch
            :type ask_scm_branch_on_launch: boolean, required, default False
            :param ask_diff_mode_on_launch: Ask diff mode on launch
            :type ask_diff_mode_on_launch: boolean, required, default False
            :param ask_variables_on_launch: Ask variables on launch
            :type ask_variables_on_launch: boolean, required, default False
            :param ask_limit_on_launch: Ask limit on launch
            :type ask_limit_on_launch: boolean, required, default False
            :param ask_tags_on_launch: Ask tags on launch
            :type ask_tags_on_launch: boolean, required, default False
            :param ask_skip_tags_on_launch: Ask skip tags on launch
            :type ask_skip_tags_on_launch: boolean, required, default False
            :param ask_job_type_on_launch: Ask job type on launch
            :type ask_job_type_on_launch: boolean, required, default False
            :param ask_verbosity_on_launch: Ask verbosity on launch
            :type ask_verbosity_on_launch: boolean, required, default False
            :param ask_inventory_on_launch: Ask inventory on launch
            :type ask_inventory_on_launch: boolean, required, default False
            :param ask_credential_on_launch: Ask credential on launch
            :type ask_credential_on_launch: boolean, required, default False
            :param survey_enabled: Survey enabled
            :type survey_enabled: boolean, required, default False
            :param become_enabled: Become enabled
            :type become_enabled: boolean, required, default False
            :param diff_mode: If enabled, textual changes made to any templated files on 
                the host are shown in the standard output
            :type diff_mode: boolean, required, default False
            :param allow_simultaneous: Allow simultaneous
            :type allow_simultaneous: boolean, required, default False
            :param custom_virtualenv: Local absolute file path containing a custom Python 
                virtualenv to use
            :type custom_virtualenv: string, required, default "None"
            :param job_slice_count: The number of jobs to slice into at runtime. Will cause the 
                Job Template to launch a workflow if value is greater than
            :type job_slice_count: integer, required, default 1
            :param webhook_service: Service that webhook requests will be accepted from
                | : ---------
                | github: GitHub
                | gitlab: GitLab
            :type webhook_service: choice, required, default ``
            :param webhook_credential: Personal Access Token for posting back the status to the 
                service API
            :type webhook_credential: id, required, default ``

        Read Only Attributes:
            :param id: Database ID for this job template.
            :type id: integer, readonly
            :param type: Data type for this job template.
                | job_template: Job Template
            :type type: choice, readonly
            :param url: URL for this job template.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this job template was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this job template was last modified.
            :type modified: datetime, readonly
            :param organization: The organization used to determine access to this template.
            :type organization: id, readonly
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
            :type status: choice, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this job template."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this job template."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this job template."""
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
        """Timestamp when this job template was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this job template was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this job template."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this job template."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

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
    def project(self):
        """Project"""
        return self._data.get("project")

    @project.setter
    def project(self, value):
        set_changes(self, "project", value, types.ID)

    @property
    def playbook(self):
        """Playbook"""
        return self._data.get("playbook")

    @playbook.setter
    def playbook(self, value):
        set_changes(self, "playbook", value, types.STRING)

    @property
    def scm_branch(self):
        """Branch to use in job run. Project default used if blank. Only allowed if project allow_override field is 
        set to true."""
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
        set_changes(self, "scm_branch", value, types.STRING)

    @property
    def forks(self):
        """Forks"""
        return self._data.get("forks")

    @forks.setter
    def forks(self, value):
        set_changes(self, "forks", value, types.INTEGER)

    @property
    def limit(self):
        """Limit"""
        return self._data.get("limit")

    @limit.setter
    def limit(self, value):
        set_changes(self, "limit", value, types.STRING)

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
        set_changes(self, "extra_vars", value, types.JSON)

    @property
    def job_tags(self):
        """Job tags"""
        return self._data.get("job_tags")

    @job_tags.setter
    def job_tags(self, value):
        set_changes(self, "job_tags", value, types.STRING)

    @property
    def force_handlers(self):
        """Force handlers"""
        return self._data.get("force_handlers")

    @force_handlers.setter
    def force_handlers(self, value):
        set_changes(self, "force_handlers", value, types.BOOLEAN)

    @property
    def skip_tags(self):
        """Skip tags"""
        return self._data.get("skip_tags")

    @skip_tags.setter
    def skip_tags(self, value):
        set_changes(self, "skip_tags", value, types.STRING)

    @property
    def start_at_task(self):
        """Start at task"""
        return self._data.get("start_at_task")

    @start_at_task.setter
    def start_at_task(self, value):
        set_changes(self, "start_at_task", value, types.STRING)

    @property
    def timeout(self):
        """The amount of time (in seconds) to run before the task is canceled."""
        return self._data.get("timeout")

    @timeout.setter
    def timeout(self, value):
        set_changes(self, "timeout", value, types.INTEGER)

    @property
    def use_fact_cache(self):
        """If enabled, Tower will act as an Ansible Fact Cache Plugin; persisting facts at the end of a playbook run 
        to the database and caching facts for use by Ansible."""
        return self._data.get("use_fact_cache")

    @use_fact_cache.setter
    def use_fact_cache(self, value):
        set_changes(self, "use_fact_cache", value, types.BOOLEAN)

    @property
    def organization(self):
        """The organization used to determine access to this template."""
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
    def host_config_key(self):
        """Host config key"""
        return self._data.get("host_config_key")

    @host_config_key.setter
    def host_config_key(self, value):
        set_changes(self, "host_config_key", value, types.STRING)

    @property
    def ask_scm_branch_on_launch(self):
        """Ask scm branch on launch"""
        return self._data.get("ask_scm_branch_on_launch")

    @ask_scm_branch_on_launch.setter
    def ask_scm_branch_on_launch(self, value):
        set_changes(self, "ask_scm_branch_on_launch", value, types.BOOLEAN)

    @property
    def ask_diff_mode_on_launch(self):
        """Ask diff mode on launch"""
        return self._data.get("ask_diff_mode_on_launch")

    @ask_diff_mode_on_launch.setter
    def ask_diff_mode_on_launch(self, value):
        set_changes(self, "ask_diff_mode_on_launch", value, types.BOOLEAN)

    @property
    def ask_variables_on_launch(self):
        """Ask variables on launch"""
        return self._data.get("ask_variables_on_launch")

    @ask_variables_on_launch.setter
    def ask_variables_on_launch(self, value):
        set_changes(self, "ask_variables_on_launch", value, types.BOOLEAN)

    @property
    def ask_limit_on_launch(self):
        """Ask limit on launch"""
        return self._data.get("ask_limit_on_launch")

    @ask_limit_on_launch.setter
    def ask_limit_on_launch(self, value):
        set_changes(self, "ask_limit_on_launch", value, types.BOOLEAN)

    @property
    def ask_tags_on_launch(self):
        """Ask tags on launch"""
        return self._data.get("ask_tags_on_launch")

    @ask_tags_on_launch.setter
    def ask_tags_on_launch(self, value):
        set_changes(self, "ask_tags_on_launch", value, types.BOOLEAN)

    @property
    def ask_skip_tags_on_launch(self):
        """Ask skip tags on launch"""
        return self._data.get("ask_skip_tags_on_launch")

    @ask_skip_tags_on_launch.setter
    def ask_skip_tags_on_launch(self, value):
        set_changes(self, "ask_skip_tags_on_launch", value, types.BOOLEAN)

    @property
    def ask_job_type_on_launch(self):
        """Ask job type on launch"""
        return self._data.get("ask_job_type_on_launch")

    @ask_job_type_on_launch.setter
    def ask_job_type_on_launch(self, value):
        set_changes(self, "ask_job_type_on_launch", value, types.BOOLEAN)

    @property
    def ask_verbosity_on_launch(self):
        """Ask verbosity on launch"""
        return self._data.get("ask_verbosity_on_launch")

    @ask_verbosity_on_launch.setter
    def ask_verbosity_on_launch(self, value):
        set_changes(self, "ask_verbosity_on_launch", value, types.BOOLEAN)

    @property
    def ask_inventory_on_launch(self):
        """Ask inventory on launch"""
        return self._data.get("ask_inventory_on_launch")

    @ask_inventory_on_launch.setter
    def ask_inventory_on_launch(self, value):
        set_changes(self, "ask_inventory_on_launch", value, types.BOOLEAN)

    @property
    def ask_credential_on_launch(self):
        """Ask credential on launch"""
        return self._data.get("ask_credential_on_launch")

    @ask_credential_on_launch.setter
    def ask_credential_on_launch(self, value):
        set_changes(self, "ask_credential_on_launch", value, types.BOOLEAN)

    @property
    def survey_enabled(self):
        """Survey enabled"""
        return self._data.get("survey_enabled")

    @survey_enabled.setter
    def survey_enabled(self, value):
        set_changes(self, "survey_enabled", value, types.BOOLEAN)

    @property
    def become_enabled(self):
        """Become enabled"""
        return self._data.get("become_enabled")

    @become_enabled.setter
    def become_enabled(self, value):
        set_changes(self, "become_enabled", value, types.BOOLEAN)

    @property
    def diff_mode(self):
        """If enabled, textual changes made to any templated files on the host are shown in the standard output"""
        return self._data.get("diff_mode")

    @diff_mode.setter
    def diff_mode(self, value):
        set_changes(self, "diff_mode", value, types.BOOLEAN)

    @property
    def allow_simultaneous(self):
        """Allow simultaneous"""
        return self._data.get("allow_simultaneous")

    @allow_simultaneous.setter
    def allow_simultaneous(self, value):
        set_changes(self, "allow_simultaneous", value, types.BOOLEAN)

    @property
    def custom_virtualenv(self):
        """Local absolute file path containing a custom Python virtualenv to use"""
        return self._data.get("custom_virtualenv")

    @custom_virtualenv.setter
    def custom_virtualenv(self, value):
        set_changes(self, "custom_virtualenv", value, types.STRING)

    @property
    def job_slice_count(self):
        """The number of jobs to slice into at runtime. Will cause the Job Template to launch a workflow if value is 
        greater than 1."""
        return self._data.get("job_slice_count")

    @job_slice_count.setter
    def job_slice_count(self, value):
        set_changes(self, "job_slice_count", value, types.INTEGER)

    @property
    def webhook_service(self):
        """Service that webhook requests will be accepted from"""
        return self._data.get("webhook_service")

    @webhook_service.setter
    def webhook_service(self, value):
        allowed_values = [
            "",
            "github",
            "gitlab"
        ]
        set_changes(self, "webhook_service", value, types.CHOICE, allowed_values)

    @property
    def webhook_credential(self):
        """Personal Access Token for posting back the status to the service API"""
        return self._data.get("webhook_credential")

    @webhook_credential.setter
    def webhook_credential(self, value):
        set_changes(self, "webhook_credential", value, types.ID)


class Job(DataModelMixin):
    __endpoint__ = "/api/v2/jobs"

    def __init__(self, **kwargs):
        """
        Job List

        Read Only Attributes:
            :param id: Database ID for this job.
            :type id: integer, readonly
            :param type: Data type for this job.
                | job: Playbook Run
            :type type: choice, readonly
            :param url: URL for this job.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this job was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this job was last modified.
            :type modified: datetime, readonly
            :param name: Name of this job.
            :type name: string, readonly
            :param description: Optional description of this job.
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
            :param controller_node: The instance that managed the isolated execution 
                environment.
            :type controller_node: string, readonly
            :param job_type: Job type
                | run: Run
                | check: Check
                | scan: Scan
            :type job_type: choice, readonly
            :param inventory: Inventory
            :type inventory: id, readonly
            :param project: Project
            :type project: id, readonly
            :param playbook: Playbook
            :type playbook: string, readonly
            :param scm_branch: Branch to use in job run. Project default used if blank. 
                Only allowed if project allow_override field is set to
            :type scm_branch: string, readonly
            :param forks: Forks
            :type forks: integer, readonly
            :param limit: Limit
            :type limit: string, readonly
            :param verbosity: Verbosity
                | 0: 0 (Normal)
                | 1: 1 (Verbose)
                | 2: 2 (More Verbose)
                | 3: 3 (Debug)
                | 4: 4 (Connection Debug)
                | 5: 5 (WinRM Debug)
            :type verbosity: choice, readonly
            :param extra_vars: Extra vars
            :type extra_vars: json, readonly
            :param job_tags: Job tags
            :type job_tags: string, readonly
            :param force_handlers: Force handlers
            :type force_handlers: boolean, readonly
            :param skip_tags: Skip tags
            :type skip_tags: string, readonly
            :param start_at_task: Start at task
            :type start_at_task: string, readonly
            :param timeout: The amount of time (in seconds) to run before the task is 
                canceled.
            :type timeout: integer, readonly
            :param use_fact_cache: If enabled, Tower will act as an Ansible Fact Cache Plugin; 
                persisting facts at the end of a playbook run to the
            :type use_fact_cache: boolean, readonly
            :param organization: The organization used to determine access to this unified 
                job.
            :type organization: id, readonly
            :param job_template: Job template
            :type job_template: id, readonly
            :param passwords_needed_to_start: Passwords needed to start
            :type passwords_needed_to_start: field, readonly
            :param allow_simultaneous: Allow simultaneous
            :type allow_simultaneous: boolean, readonly
            :param artifacts: Artifacts
            :type artifacts: json, readonly
            :param scm_revision: The SCM Revision from the Project used for this job, if 
                available
            :type scm_revision: string, readonly
            :param instance_group: The Instance group the job was run under
            :type instance_group: id, readonly
            :param diff_mode: If enabled, textual changes made to any templated files on 
                the host are shown in the standard output
            :type diff_mode: boolean, readonly
            :param job_slice_number: If part of a sliced job, the ID of the inventory slice 
                operated on. If not part of sliced job, parameter is not
            :type job_slice_number: integer, readonly
            :param job_slice_count: If ran as part of sliced jobs, the total number of slices. 
                If 1, job is not part of a sliced job.
            :type job_slice_count: integer, readonly
            :param webhook_service: Service that webhook requests will be accepted from
                | : ---------
                | github: GitHub
                | gitlab: GitLab
            :type webhook_service: choice, readonly
            :param webhook_credential: Personal Access Token for posting back the status to the 
                service API
            :type webhook_credential: id, readonly
            :param webhook_guid: Unique identifier of the event that triggered this webhook
            :type webhook_guid: string, readonly
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
            :param host_status_counts: A count of hosts uniquely assigned to each status.
            :type host_status_counts: field, readonly
            :param playbook_counts: A count of all plays and tasks for the job run.
            :type playbook_counts: field, readonly
            :param custom_virtualenv: Custom virtualenv
            :type custom_virtualenv: string, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this job."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this job."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this job."""
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
        """Timestamp when this job was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this job was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this job."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this job."""
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
        raise ValueReadOnly

    @property
    def inventory(self):
        """Inventory"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        raise ValueReadOnly

    @property
    def project(self):
        """Project"""
        return self._data.get("project")

    @project.setter
    def project(self, value):
        raise ValueReadOnly

    @property
    def playbook(self):
        """Playbook"""
        return self._data.get("playbook")

    @playbook.setter
    def playbook(self, value):
        raise ValueReadOnly

    @property
    def scm_branch(self):
        """Branch to use in job run. Project default used if blank. Only allowed if project allow_override field is 
        set to true."""
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
        raise ValueReadOnly

    @property
    def forks(self):
        """Forks"""
        return self._data.get("forks")

    @forks.setter
    def forks(self, value):
        raise ValueReadOnly

    @property
    def limit(self):
        """Limit"""
        return self._data.get("limit")

    @limit.setter
    def limit(self, value):
        raise ValueReadOnly

    @property
    def verbosity(self):
        """Verbosity"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        raise ValueReadOnly

    @property
    def extra_vars(self):
        """Extra vars"""
        return self._data.get("extra_vars")

    @extra_vars.setter
    def extra_vars(self, value):
        raise ValueReadOnly

    @property
    def job_tags(self):
        """Job tags"""
        return self._data.get("job_tags")

    @job_tags.setter
    def job_tags(self, value):
        raise ValueReadOnly

    @property
    def force_handlers(self):
        """Force handlers"""
        return self._data.get("force_handlers")

    @force_handlers.setter
    def force_handlers(self, value):
        raise ValueReadOnly

    @property
    def skip_tags(self):
        """Skip tags"""
        return self._data.get("skip_tags")

    @skip_tags.setter
    def skip_tags(self, value):
        raise ValueReadOnly

    @property
    def start_at_task(self):
        """Start at task"""
        return self._data.get("start_at_task")

    @start_at_task.setter
    def start_at_task(self, value):
        raise ValueReadOnly

    @property
    def timeout(self):
        """The amount of time (in seconds) to run before the task is canceled."""
        return self._data.get("timeout")

    @timeout.setter
    def timeout(self, value):
        raise ValueReadOnly

    @property
    def use_fact_cache(self):
        """If enabled, Tower will act as an Ansible Fact Cache Plugin; persisting facts at the end of a playbook run 
        to the database and caching facts for use by Ansible."""
        return self._data.get("use_fact_cache")

    @use_fact_cache.setter
    def use_fact_cache(self, value):
        raise ValueReadOnly

    @property
    def organization(self):
        """The organization used to determine access to this unified job."""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        raise ValueReadOnly

    @property
    def job_template(self):
        """Job template"""
        return self._data.get("job_template")

    @job_template.setter
    def job_template(self, value):
        raise ValueReadOnly

    @property
    def passwords_needed_to_start(self):
        """Passwords needed to start"""
        return self._data.get("passwords_needed_to_start")

    @passwords_needed_to_start.setter
    def passwords_needed_to_start(self, value):
        raise ValueReadOnly

    @property
    def allow_simultaneous(self):
        """Allow simultaneous"""
        return self._data.get("allow_simultaneous")

    @allow_simultaneous.setter
    def allow_simultaneous(self, value):
        raise ValueReadOnly

    @property
    def artifacts(self):
        """Artifacts"""
        return self._data.get("artifacts")

    @artifacts.setter
    def artifacts(self, value):
        raise ValueReadOnly

    @property
    def scm_revision(self):
        """The SCM Revision from the Project used for this job, if available"""
        return self._data.get("scm_revision")

    @scm_revision.setter
    def scm_revision(self, value):
        raise ValueReadOnly

    @property
    def instance_group(self):
        """The Instance group the job was run under"""
        return self._data.get("instance_group")

    @instance_group.setter
    def instance_group(self, value):
        raise ValueReadOnly

    @property
    def diff_mode(self):
        """If enabled, textual changes made to any templated files on the host are shown in the standard output"""
        return self._data.get("diff_mode")

    @diff_mode.setter
    def diff_mode(self, value):
        raise ValueReadOnly

    @property
    def job_slice_number(self):
        """If part of a sliced job, the ID of the inventory slice operated on. If not part of sliced job, parameter 
        is not used."""
        return self._data.get("job_slice_number")

    @job_slice_number.setter
    def job_slice_number(self, value):
        raise ValueReadOnly

    @property
    def job_slice_count(self):
        """If ran as part of sliced jobs, the total number of slices. If 1, job is not part of a sliced job."""
        return self._data.get("job_slice_count")

    @job_slice_count.setter
    def job_slice_count(self, value):
        raise ValueReadOnly

    @property
    def webhook_service(self):
        """Service that webhook requests will be accepted from"""
        return self._data.get("webhook_service")

    @webhook_service.setter
    def webhook_service(self, value):
        raise ValueReadOnly

    @property
    def webhook_credential(self):
        """Personal Access Token for posting back the status to the service API"""
        return self._data.get("webhook_credential")

    @webhook_credential.setter
    def webhook_credential(self, value):
        raise ValueReadOnly

    @property
    def webhook_guid(self):
        """Unique identifier of the event that triggered this webhook"""
        return self._data.get("webhook_guid")

    @webhook_guid.setter
    def webhook_guid(self, value):
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
    def host_status_counts(self):
        """A count of hosts uniquely assigned to each status."""
        return self._data.get("host_status_counts")

    @host_status_counts.setter
    def host_status_counts(self, value):
        raise ValueReadOnly

    @property
    def playbook_counts(self):
        """A count of all plays and tasks for the job run."""
        return self._data.get("playbook_counts")

    @playbook_counts.setter
    def playbook_counts(self, value):
        raise ValueReadOnly

    @property
    def custom_virtualenv(self):
        """Custom virtualenv"""
        return self._data.get("custom_virtualenv")

    @custom_virtualenv.setter
    def custom_virtualenv(self, value):
        raise ValueReadOnly


class JobEvent(DataModelMixin):
    __endpoint__ = "/api/v2/job_events"

    def __init__(self, **kwargs):
        """
        Job Event List

        Read Only Attributes:
            :param id: Database ID for this job event.
            :type id: integer, readonly
            :param type: Data type for this job event.
                | job_event: Job Event
            :type type: choice, readonly
            :param url: URL for this job event.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this job event was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this job event was last modified.
            :type modified: datetime, readonly
            :param job: Job
            :type job: id, readonly
            :param event: Event
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
            :type event: choice, readonly
            :param counter: Counter
            :type counter: integer, readonly
            :param event_display: Event display
            :type event_display: string, readonly
            :param event_data: Event data
            :type event_data: json, readonly
            :param event_level: Event level
            :type event_level: integer, readonly
            :param failed: Failed
            :type failed: boolean, readonly
            :param changed: Changed
            :type changed: boolean, readonly
            :param uuid: Uuid
            :type uuid: string, readonly
            :param parent_uuid: Parent uuid
            :type parent_uuid: string, readonly
            :param host: Host
            :type host: id, readonly
            :param host_name: Host name
            :type host_name: string, readonly
            :param playbook: Playbook
            :type playbook: string, readonly
            :param play: Play
            :type play: string, readonly
            :param task: Task
            :type task: string, readonly
            :param role: Role
            :type role: string, readonly
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
        """Database ID for this job event."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this job event."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this job event."""
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
        """Timestamp when this job event was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this job event was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def job(self):
        """Job"""
        return self._data.get("job")

    @job.setter
    def job(self, value):
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
    def event_level(self):
        """Event level"""
        return self._data.get("event_level")

    @event_level.setter
    def event_level(self, value):
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
    def parent_uuid(self):
        """Parent uuid"""
        return self._data.get("parent_uuid")

    @parent_uuid.setter
    def parent_uuid(self, value):
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
    def playbook(self):
        """Playbook"""
        return self._data.get("playbook")

    @playbook.setter
    def playbook(self, value):
        raise ValueReadOnly

    @property
    def play(self):
        """Play"""
        return self._data.get("play")

    @play.setter
    def play(self, value):
        raise ValueReadOnly

    @property
    def task(self):
        """Task"""
        return self._data.get("task")

    @task.setter
    def task(self, value):
        raise ValueReadOnly

    @property
    def role(self):
        """Role"""
        return self._data.get("role")

    @role.setter
    def role(self, value):
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


class SystemJob(DataModelMixin):
    __endpoint__ = "/api/v2/system_jobs"

    def __init__(self, **kwargs):
        """
        System Job List

        Read Only Attributes:
            :param id: Database ID for this system job.
            :type id: integer, readonly
            :param type: Data type for this system job.
                | system_job: Management Job
            :type type: choice, readonly
            :param url: URL for this system job.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this system job was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this system job was last modified.
            :type modified: datetime, readonly
            :param name: Name of this system job.
            :type name: string, readonly
            :param description: Optional description of this system job.
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
            :param system_job_template: System job template
            :type system_job_template: id, readonly
            :param job_type: Job type
                | : ---------
                | cleanup_jobs: Remove jobs older than a certain number of days
                | cleanup_activitystream: Remove activity stream entries older than a certain number of days
                | cleanup_sessions: Removes expired browser sessions from the database
                | cleanup_tokens: Removes expired OAuth 2 access tokens and refresh tokens
            :type job_type: choice, readonly
            :param extra_vars: Extra vars
            :type extra_vars: string, readonly
            :param result_stdout: Result stdout
            :type result_stdout: field, readonly
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
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this system job."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this system job."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this system job."""
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
        """Timestamp when this system job was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this system job was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this system job."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this system job."""
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
    def system_job_template(self):
        """System job template"""
        return self._data.get("system_job_template")

    @system_job_template.setter
    def system_job_template(self, value):
        raise ValueReadOnly

    @property
    def job_type(self):
        """Job type"""
        return self._data.get("job_type")

    @job_type.setter
    def job_type(self, value):
        raise ValueReadOnly

    @property
    def extra_vars(self):
        """Extra vars"""
        return self._data.get("extra_vars")

    @extra_vars.setter
    def extra_vars(self, value):
        raise ValueReadOnly

    @property
    def result_stdout(self):
        """Result stdout"""
        return self._data.get("result_stdout")

    @result_stdout.setter
    def result_stdout(self, value):
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


class SystemJobTemplate(DataModelMixin):
    __endpoint__ = "/api/v2/system_job_templates"

    def __init__(self, **kwargs):
        """
        System Job Template List

        Read Only Attributes:
            :param id: Database ID for this system job template.
            :type id: integer, readonly
            :param type: Data type for this system job template.
                | system_job_template: System Job Template
            :type type: choice, readonly
            :param url: URL for this system job template.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this system job template was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this system job template was last modified.
            :type modified: datetime, readonly
            :param name: Name of this system job template.
            :type name: string, readonly
            :param description: Optional description of this system job template.
            :type description: string, readonly
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
                | ok: OK
                | missing: Missing
                | none: No External Source
                | updating: Updating
            :type status: choice, readonly
            :param job_type: Job type
                | : ---------
                | cleanup_jobs: Remove jobs older than a certain number of days
                | cleanup_activitystream: Remove activity stream entries older than a certain number of days
                | cleanup_sessions: Removes expired browser sessions from the database
                | cleanup_tokens: Removes expired OAuth 2 access tokens and refresh tokens
            :type job_type: choice, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this system job template."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this system job template."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this system job template."""
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
        """Timestamp when this system job template was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this system job template was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this system job template."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this system job template."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
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
    def job_type(self):
        """Job type"""
        return self._data.get("job_type")

    @job_type.setter
    def job_type(self, value):
        raise ValueReadOnly


class Schedule(DataModelMixin):
    __endpoint__ = "/api/v2/schedules"

    def __init__(self, **kwargs):
        """
        Schedules

        Attributes:
            :param rrule: A value representing the schedules iCal recurrence rule.
            :type rrule: string, required, default ``
            :param name: Name of this schedule.
            :type name: string, required, default ``
            :param description: Optional description of this schedule.
            :type description: string, required, default ""
            :param extra_data: Extra data
            :type extra_data: json, required, default "{}"
            :param inventory: Inventory applied as a prompt, assuming job template 
                prompts for inventory
            :type inventory: id, required, default ``
            :param scm_branch: Scm branch
            :type scm_branch: string, required, default "None"
            :param job_type: Job type
                | None: ---------
                | : ---------
                | run: Run
                | check: Check
            :type job_type: choice, required, default "None"
            :param job_tags: Job tags
            :type job_tags: string, required, default "None"
            :param skip_tags: Skip tags
            :type skip_tags: string, required, default "None"
            :param limit: Limit
            :type limit: string, required, default "None"
            :param diff_mode: Diff mode
            :type diff_mode: boolean, required, default "None"
            :param verbosity: Verbosity
                | None: ---------
                | 0: 0 (Normal)
                | 1: 1 (Verbose)
                | 2: 2 (More Verbose)
                | 3: 3 (Debug)
                | 4: 4 (Connection Debug)
                | 5: 5 (WinRM Debug)
            :type verbosity: choice, required, default "None"
            :param unified_job_template: Unified job template
            :type unified_job_template: id, required, default ``
            :param enabled: Enables processing of this schedule.
            :type enabled: boolean, required, default True

        Read Only Attributes:
            :param id: Database ID for this schedule.
            :type id: integer, readonly
            :param type: Data type for this schedule.
                | schedule: Schedule
            :type type: choice, readonly
            :param url: URL for this schedule.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this schedule was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this schedule was last modified.
            :type modified: datetime, readonly
            :param dtstart: The first occurrence of the schedule occurs on or after 
                this time.
            :type dtstart: datetime, readonly
            :param dtend: The last occurrence of the schedule occurs before this 
                time, aftewards the schedule expires.
            :type dtend: datetime, readonly
            :param next_run: The next time that the scheduled action will run.
            :type next_run: datetime, readonly
            :param timezone: Timezone
            :type timezone: field, readonly
            :param until: Until
            :type until: field, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def rrule(self):
        """A value representing the schedules iCal recurrence rule."""
        return self._data.get("rrule")

    @rrule.setter
    def rrule(self, value):
        set_changes(self, "rrule", value, types.STRING)

    @property
    def id(self):
        """Database ID for this schedule."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this schedule."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this schedule."""
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
        """Timestamp when this schedule was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this schedule was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this schedule."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this schedule."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def extra_data(self):
        """Extra data"""
        return self._data.get("extra_data")

    @extra_data.setter
    def extra_data(self, value):
        set_changes(self, "extra_data", value, types.JSON)

    @property
    def inventory(self):
        """Inventory applied as a prompt, assuming job template prompts for inventory"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        set_changes(self, "inventory", value, types.ID)

    @property
    def scm_branch(self):
        """Scm branch"""
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
        set_changes(self, "scm_branch", value, types.STRING)

    @property
    def job_type(self):
        """Job type"""
        return self._data.get("job_type")

    @job_type.setter
    def job_type(self, value):
        allowed_values = [
            "None",
            "",
            "run",
            "check"
        ]
        set_changes(self, "job_type", value, types.CHOICE, allowed_values)

    @property
    def job_tags(self):
        """Job tags"""
        return self._data.get("job_tags")

    @job_tags.setter
    def job_tags(self, value):
        set_changes(self, "job_tags", value, types.STRING)

    @property
    def skip_tags(self):
        """Skip tags"""
        return self._data.get("skip_tags")

    @skip_tags.setter
    def skip_tags(self, value):
        set_changes(self, "skip_tags", value, types.STRING)

    @property
    def limit(self):
        """Limit"""
        return self._data.get("limit")

    @limit.setter
    def limit(self, value):
        set_changes(self, "limit", value, types.STRING)

    @property
    def diff_mode(self):
        """Diff mode"""
        return self._data.get("diff_mode")

    @diff_mode.setter
    def diff_mode(self, value):
        set_changes(self, "diff_mode", value, types.BOOLEAN)

    @property
    def verbosity(self):
        """Verbosity"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        allowed_values = [
            "None",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5"
        ]
        set_changes(self, "verbosity", value, types.CHOICE, allowed_values)

    @property
    def unified_job_template(self):
        """Unified job template"""
        return self._data.get("unified_job_template")

    @unified_job_template.setter
    def unified_job_template(self, value):
        set_changes(self, "unified_job_template", value, types.ID)

    @property
    def enabled(self):
        """Enables processing of this schedule."""
        return self._data.get("enabled")

    @enabled.setter
    def enabled(self, value):
        set_changes(self, "enabled", value, types.BOOLEAN)

    @property
    def dtstart(self):
        """The first occurrence of the schedule occurs on or after this time."""
        return self._data.get("dtstart")

    @dtstart.setter
    def dtstart(self, value):
        raise ValueReadOnly

    @property
    def dtend(self):
        """The last occurrence of the schedule occurs before this time, aftewards the schedule expires."""
        return self._data.get("dtend")

    @dtend.setter
    def dtend(self, value):
        raise ValueReadOnly

    @property
    def next_run(self):
        """The next time that the scheduled action will run."""
        return self._data.get("next_run")

    @next_run.setter
    def next_run(self, value):
        raise ValueReadOnly

    @property
    def timezone(self):
        """Timezone"""
        return self._data.get("timezone")

    @timezone.setter
    def timezone(self, value):
        raise ValueReadOnly

    @property
    def until(self):
        """Until"""
        return self._data.get("until")

    @until.setter
    def until(self, value):
        raise ValueReadOnly


class ActivityStream(DataModelMixin):
    __endpoint__ = "/api/v2/activity_stream"

    def __init__(self, **kwargs):
        """
        Activity Stream List

        Read Only Attributes:
            :param id: Database ID for this activity stream.
            :type id: integer, readonly
            :param type: Data type for this activity stream.
                | activity_stream: Activity Stream
            :type type: choice, readonly
            :param url: URL for this activity stream.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param timestamp: Timestamp
            :type timestamp: datetime, readonly
            :param operation: The action taken with respect to the given object(s).
                | create: Entity Created
                | update: Entity Updated
                | delete: Entity Deleted
                | associate: Entity Associated with another Entity
                | disassociate: Entity was Disassociated with another Entity
            :type operation: choice, readonly
            :param changes: A summary of the new and changed values when an object is 
                created, updated, or deleted
            :type changes: json, readonly
            :param object1: For create, update, and delete events this is the object 
                type that was affected. For associate and disassociate 
                d
            :type object1: string, readonly
            :param object2: Unpopulated for create, update, and delete events. For 
                associate and disassociate events this is the object type
            :type object2: string, readonly
            :param object_association: When present, shows the field name of the role or 
                relationship that changed.
            :type object_association: field, readonly
            :param action_node: The cluster node the activity took place on.
            :type action_node: string, readonly
            :param object_type: When present, shows the model on which the role or 
                relationship was defined.
            :type object_type: field, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this activity stream."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this activity stream."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this activity stream."""
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
    def timestamp(self):
        """Timestamp"""
        return self._data.get("timestamp")

    @timestamp.setter
    def timestamp(self, value):
        raise ValueReadOnly

    @property
    def operation(self):
        """The action taken with respect to the given object(s)."""
        return self._data.get("operation")

    @operation.setter
    def operation(self, value):
        raise ValueReadOnly

    @property
    def changes(self):
        """A summary of the new and changed values when an object is created, updated, or deleted"""
        return self._data.get("changes")

    @changes.setter
    def changes(self, value):
        raise ValueReadOnly

    @property
    def object1(self):
        """For create, update, and delete events this is the object type that was affected. For associate and 
        disassociate events this is the object type associated or disassociated with object2."""
        return self._data.get("object1")

    @object1.setter
    def object1(self, value):
        raise ValueReadOnly

    @property
    def object2(self):
        """Unpopulated for create, update, and delete events. For associate and disassociate events this is the 
        object type that object1 is being associated with."""
        return self._data.get("object2")

    @object2.setter
    def object2(self, value):
        raise ValueReadOnly

    @property
    def object_association(self):
        """When present, shows the field name of the role or relationship that changed."""
        return self._data.get("object_association")

    @object_association.setter
    def object_association(self, value):
        raise ValueReadOnly

    @property
    def action_node(self):
        """The cluster node the activity took place on."""
        return self._data.get("action_node")

    @action_node.setter
    def action_node(self, value):
        raise ValueReadOnly

    @property
    def object_type(self):
        """When present, shows the model on which the role or relationship was defined."""
        return self._data.get("object_type")

    @object_type.setter
    def object_type(self, value):
        raise ValueReadOnly
