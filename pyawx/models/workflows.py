from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class WorkflowJobTemplate(DataModelMixin):
    __endpoint__ = "/api/v2/workflow_job_templates"

    def __init__(self, **kwargs):
        """
        Workflow Job Template List

        Attributes:
            :param name: Name of this workflow job template.
            :type name: string, required, default ``
            :param description: Optional description of this workflow job template.
            :type description: string, required, default ""
            :param extra_vars: Extra vars
            :type extra_vars: json, required, default ""
            :param organization: The organization used to determine access to this template.
            :type organization: id, required, default ``
            :param survey_enabled: Survey enabled
            :type survey_enabled: boolean, required, default False
            :param allow_simultaneous: Allow simultaneous
            :type allow_simultaneous: boolean, required, default False
            :param ask_variables_on_launch: Ask variables on launch
            :type ask_variables_on_launch: boolean, required, default False
            :param inventory: Inventory applied as a prompt, assuming job template 
                prompts for inventory
            :type inventory: id, required, default ``
            :param limit: Limit
            :type limit: string, required, default "None"
            :param scm_branch: Scm branch
            :type scm_branch: string, required, default "None"
            :param ask_inventory_on_launch: Ask inventory on launch
            :type ask_inventory_on_launch: boolean, required, default False
            :param ask_scm_branch_on_launch: Ask scm branch on launch
            :type ask_scm_branch_on_launch: boolean, required, default False
            :param ask_limit_on_launch: Ask limit on launch
            :type ask_limit_on_launch: boolean, required, default False
            :param webhook_service: Service that webhook requests will be accepted from
                | : ---------
                | github: GitHub
                | gitlab: GitLab
            :type webhook_service: choice, required, default ``
            :param webhook_credential: Personal Access Token for posting back the status to the 
                service API
            :type webhook_credential: id, required, default ``

        Read Only Attributes:
            :param id: Database ID for this workflow job template.
            :type id: integer, readonly
            :param type: Data type for this workflow job template.
                | workflow_job_template: Workflow Template
            :type type: choice, readonly
            :param url: URL for this workflow job template.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this workflow job template was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this workflow job template was last 
                modified.
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
                | ok: OK
                | missing: Missing
                | none: No External Source
                | updating: Updating
            :type status: choice, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this workflow job template."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this workflow job template."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this workflow job template."""
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
        """Timestamp when this workflow job template was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this workflow job template was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this workflow job template."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this workflow job template."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

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
    def extra_vars(self):
        """Extra vars"""
        return self._data.get("extra_vars")

    @extra_vars.setter
    def extra_vars(self, value):
        set_changes(self, "extra_vars", value, types.JSON)

    @property
    def organization(self):
        """The organization used to determine access to this template."""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.ID)

    @property
    def survey_enabled(self):
        """Survey enabled"""
        return self._data.get("survey_enabled")

    @survey_enabled.setter
    def survey_enabled(self, value):
        set_changes(self, "survey_enabled", value, types.BOOLEAN)

    @property
    def allow_simultaneous(self):
        """Allow simultaneous"""
        return self._data.get("allow_simultaneous")

    @allow_simultaneous.setter
    def allow_simultaneous(self, value):
        set_changes(self, "allow_simultaneous", value, types.BOOLEAN)

    @property
    def ask_variables_on_launch(self):
        """Ask variables on launch"""
        return self._data.get("ask_variables_on_launch")

    @ask_variables_on_launch.setter
    def ask_variables_on_launch(self, value):
        set_changes(self, "ask_variables_on_launch", value, types.BOOLEAN)

    @property
    def inventory(self):
        """Inventory applied as a prompt, assuming job template prompts for inventory"""
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
    def scm_branch(self):
        """Scm branch"""
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
        set_changes(self, "scm_branch", value, types.STRING)

    @property
    def ask_inventory_on_launch(self):
        """Ask inventory on launch"""
        return self._data.get("ask_inventory_on_launch")

    @ask_inventory_on_launch.setter
    def ask_inventory_on_launch(self, value):
        set_changes(self, "ask_inventory_on_launch", value, types.BOOLEAN)

    @property
    def ask_scm_branch_on_launch(self):
        """Ask scm branch on launch"""
        return self._data.get("ask_scm_branch_on_launch")

    @ask_scm_branch_on_launch.setter
    def ask_scm_branch_on_launch(self, value):
        set_changes(self, "ask_scm_branch_on_launch", value, types.BOOLEAN)

    @property
    def ask_limit_on_launch(self):
        """Ask limit on launch"""
        return self._data.get("ask_limit_on_launch")

    @ask_limit_on_launch.setter
    def ask_limit_on_launch(self, value):
        set_changes(self, "ask_limit_on_launch", value, types.BOOLEAN)

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


class WorkflowJob(DataModelMixin):
    __endpoint__ = "/api/v2/workflow_jobs"

    def __init__(self, **kwargs):
        """
        Workflow Job List

        Read Only Attributes:
            :param id: Database ID for this workflow job.
            :type id: integer, readonly
            :param type: Data type for this workflow job.
                | workflow_job: Workflow Job
            :type type: choice, readonly
            :param url: URL for this workflow job.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this workflow job was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this workflow job was last modified.
            :type modified: datetime, readonly
            :param name: Name of this workflow job.
            :type name: string, readonly
            :param description: Optional description of this workflow job.
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
            :param workflow_job_template: Workflow job template
            :type workflow_job_template: id, readonly
            :param extra_vars: Extra vars
            :type extra_vars: json, readonly
            :param allow_simultaneous: Allow simultaneous
            :type allow_simultaneous: boolean, readonly
            :param job_template: If automatically created for a sliced job run, the job 
                template the workflow job was created from.
            :type job_template: id, readonly
            :param is_sliced_job: Is sliced job
            :type is_sliced_job: boolean, readonly
            :param inventory: Inventory applied as a prompt, assuming job template 
                prompts for inventory
            :type inventory: id, readonly
            :param limit: Limit
            :type limit: string, readonly
            :param scm_branch: Scm branch
            :type scm_branch: string, readonly
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
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this workflow job."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this workflow job."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this workflow job."""
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
        """Timestamp when this workflow job was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this workflow job was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this workflow job."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this workflow job."""
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
    def workflow_job_template(self):
        """Workflow job template"""
        return self._data.get("workflow_job_template")

    @workflow_job_template.setter
    def workflow_job_template(self, value):
        raise ValueReadOnly

    @property
    def extra_vars(self):
        """Extra vars"""
        return self._data.get("extra_vars")

    @extra_vars.setter
    def extra_vars(self, value):
        raise ValueReadOnly

    @property
    def allow_simultaneous(self):
        """Allow simultaneous"""
        return self._data.get("allow_simultaneous")

    @allow_simultaneous.setter
    def allow_simultaneous(self, value):
        raise ValueReadOnly

    @property
    def job_template(self):
        """If automatically created for a sliced job run, the job template the workflow job was created from."""
        return self._data.get("job_template")

    @job_template.setter
    def job_template(self, value):
        raise ValueReadOnly

    @property
    def is_sliced_job(self):
        """Is sliced job"""
        return self._data.get("is_sliced_job")

    @is_sliced_job.setter
    def is_sliced_job(self, value):
        raise ValueReadOnly

    @property
    def inventory(self):
        """Inventory applied as a prompt, assuming job template prompts for inventory"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        raise ValueReadOnly

    @property
    def limit(self):
        """Limit"""
        return self._data.get("limit")

    @limit.setter
    def limit(self, value):
        raise ValueReadOnly

    @property
    def scm_branch(self):
        """Scm branch"""
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
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


class WorkflowApproval(DataModelMixin):
    __endpoint__ = "/api/v2/workflow_approvals"

    def __init__(self, **kwargs):
        """
        Workflow Approval List

        Attributes:
            :param name: Name of this workflow approval.
            :type name: string, required, default ``
            :param description: Optional description of this workflow approval.
            :type description: string, required, default ""

        Read Only Attributes:
            :param id: Database ID for this workflow approval.
            :type id: integer, readonly
            :param type: Data type for this workflow approval.
                | workflow_approval: Workflow Approval
            :type type: choice, readonly
            :param url: URL for this workflow approval.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this workflow approval was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this workflow approval was last modified.
            :type modified: datetime, readonly
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
            :param can_approve_or_deny: Can approve or deny
            :type can_approve_or_deny: field, readonly
            :param approval_expiration: Approval expiration
            :type approval_expiration: field, readonly
            :param timed_out: Timed out
            :type timed_out: boolean, readonly
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
        """Database ID for this workflow approval."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this workflow approval."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this workflow approval."""
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
        """Timestamp when this workflow approval was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this workflow approval was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this workflow approval."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this workflow approval."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

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
    def can_approve_or_deny(self):
        """Can approve or deny"""
        return self._data.get("can_approve_or_deny")

    @can_approve_or_deny.setter
    def can_approve_or_deny(self, value):
        raise ValueReadOnly

    @property
    def approval_expiration(self):
        """Approval expiration"""
        return self._data.get("approval_expiration")

    @approval_expiration.setter
    def approval_expiration(self, value):
        raise ValueReadOnly

    @property
    def timed_out(self):
        """Timed out"""
        return self._data.get("timed_out")

    @timed_out.setter
    def timed_out(self, value):
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


class WorkflowJobTemplateNode(DataModelMixin):
    __endpoint__ = "/api/v2/workflow_job_template_nodes"

    def __init__(self, **kwargs):
        """
        Workflow Job Template Node List

        Attributes:
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
            :param workflow_job_template: Workflow job template
            :type workflow_job_template: id, required, default ``
            :param unified_job_template: Unified job template
            :type unified_job_template: id, required, default ``
            :param all_parents_must_converge: If enabled then the node will only run if all of the parent 
                nodes have met the criteria to reach this node
            :type all_parents_must_converge: boolean, required, default False
            :param identifier: An identifier for this node that is unique within its 
                workflow. It is copied to workflow job nodes corresponding
            :type identifier: string, required, default "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

        Read Only Attributes:
            :param id: Database ID for this workflow job template node.
            :type id: integer, readonly
            :param type: Data type for this workflow job template node.
                | workflow_job_template_node: Workflow Job Template Node
            :type type: choice, readonly
            :param url: URL for this workflow job template node.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this workflow job template node was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this workflow job template node was last 
                modified.
            :type modified: datetime, readonly
            :param success_nodes: Success nodes
            :type success_nodes: field, readonly
            :param failure_nodes: Failure nodes
            :type failure_nodes: field, readonly
            :param always_nodes: Always nodes
            :type always_nodes: field, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this workflow job template node."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this workflow job template node."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this workflow job template node."""
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
        """Timestamp when this workflow job template node was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this workflow job template node was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

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
    def workflow_job_template(self):
        """Workflow job template"""
        return self._data.get("workflow_job_template")

    @workflow_job_template.setter
    def workflow_job_template(self, value):
        set_changes(self, "workflow_job_template", value, types.ID)

    @property
    def unified_job_template(self):
        """Unified job template"""
        return self._data.get("unified_job_template")

    @unified_job_template.setter
    def unified_job_template(self, value):
        set_changes(self, "unified_job_template", value, types.ID)

    @property
    def success_nodes(self):
        """Success nodes"""
        return self._data.get("success_nodes")

    @success_nodes.setter
    def success_nodes(self, value):
        raise ValueReadOnly

    @property
    def failure_nodes(self):
        """Failure nodes"""
        return self._data.get("failure_nodes")

    @failure_nodes.setter
    def failure_nodes(self, value):
        raise ValueReadOnly

    @property
    def always_nodes(self):
        """Always nodes"""
        return self._data.get("always_nodes")

    @always_nodes.setter
    def always_nodes(self, value):
        raise ValueReadOnly

    @property
    def all_parents_must_converge(self):
        """If enabled then the node will only run if all of the parent nodes have met the criteria to reach this 
        node"""
        return self._data.get("all_parents_must_converge")

    @all_parents_must_converge.setter
    def all_parents_must_converge(self, value):
        set_changes(self, "all_parents_must_converge", value, types.BOOLEAN)

    @property
    def identifier(self):
        """An identifier for this node that is unique within its workflow. It is copied to workflow job nodes 
        corresponding to this node."""
        return self._data.get("identifier")

    @identifier.setter
    def identifier(self, value):
        set_changes(self, "identifier", value, types.STRING)


class WorkflowJobNode(DataModelMixin):
    __endpoint__ = "/api/v2/workflow_job_nodes"

    def __init__(self, **kwargs):
        """
        Workflow Job Node List

        Read Only Attributes:
            :param id: Database ID for this workflow job node.
            :type id: integer, readonly
            :param type: Data type for this workflow job node.
                | workflow_job_node: Workflow Job Node
            :type type: choice, readonly
            :param url: URL for this workflow job node.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this workflow job node was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this workflow job node was last modified.
            :type modified: datetime, readonly
            :param extra_data: Extra data
            :type extra_data: json, readonly
            :param inventory: Inventory applied as a prompt, assuming job template 
                prompts for inventory
            :type inventory: id, readonly
            :param scm_branch: Scm branch
            :type scm_branch: string, readonly
            :param job_type: Job type
                | None: ---------
                | : ---------
                | run: Run
                | check: Check
            :type job_type: choice, readonly
            :param job_tags: Job tags
            :type job_tags: string, readonly
            :param skip_tags: Skip tags
            :type skip_tags: string, readonly
            :param limit: Limit
            :type limit: string, readonly
            :param diff_mode: Diff mode
            :type diff_mode: boolean, readonly
            :param verbosity: Verbosity
                | None: ---------
                | 0: 0 (Normal)
                | 1: 1 (Verbose)
                | 2: 2 (More Verbose)
                | 3: 3 (Debug)
                | 4: 4 (Connection Debug)
                | 5: 5 (WinRM Debug)
            :type verbosity: choice, readonly
            :param job: Job
            :type job: id, readonly
            :param workflow_job: Workflow job
            :type workflow_job: id, readonly
            :param unified_job_template: Unified job template
            :type unified_job_template: id, readonly
            :param success_nodes: Success nodes
            :type success_nodes: field, readonly
            :param failure_nodes: Failure nodes
            :type failure_nodes: field, readonly
            :param always_nodes: Always nodes
            :type always_nodes: field, readonly
            :param all_parents_must_converge: If enabled then the node will only run if all of the parent 
                nodes have met the criteria to reach this node
            :type all_parents_must_converge: boolean, readonly
            :param do_not_run: Indicates that a job will not be created when True. 
                Workflow runtime semantics will mark this True if the node 
                 of
            :type do_not_run: boolean, readonly
            :param identifier: An identifier coresponding to the workflow job template 
                node that this node was created from.
            :type identifier: string, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this workflow job node."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this workflow job node."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this workflow job node."""
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
        """Timestamp when this workflow job node was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this workflow job node was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def extra_data(self):
        """Extra data"""
        return self._data.get("extra_data")

    @extra_data.setter
    def extra_data(self, value):
        raise ValueReadOnly

    @property
    def inventory(self):
        """Inventory applied as a prompt, assuming job template prompts for inventory"""
        return self._data.get("inventory")

    @inventory.setter
    def inventory(self, value):
        raise ValueReadOnly

    @property
    def scm_branch(self):
        """Scm branch"""
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
        raise ValueReadOnly

    @property
    def job_type(self):
        """Job type"""
        return self._data.get("job_type")

    @job_type.setter
    def job_type(self, value):
        raise ValueReadOnly

    @property
    def job_tags(self):
        """Job tags"""
        return self._data.get("job_tags")

    @job_tags.setter
    def job_tags(self, value):
        raise ValueReadOnly

    @property
    def skip_tags(self):
        """Skip tags"""
        return self._data.get("skip_tags")

    @skip_tags.setter
    def skip_tags(self, value):
        raise ValueReadOnly

    @property
    def limit(self):
        """Limit"""
        return self._data.get("limit")

    @limit.setter
    def limit(self, value):
        raise ValueReadOnly

    @property
    def diff_mode(self):
        """Diff mode"""
        return self._data.get("diff_mode")

    @diff_mode.setter
    def diff_mode(self, value):
        raise ValueReadOnly

    @property
    def verbosity(self):
        """Verbosity"""
        return self._data.get("verbosity")

    @verbosity.setter
    def verbosity(self, value):
        raise ValueReadOnly

    @property
    def job(self):
        """Job"""
        return self._data.get("job")

    @job.setter
    def job(self, value):
        raise ValueReadOnly

    @property
    def workflow_job(self):
        """Workflow job"""
        return self._data.get("workflow_job")

    @workflow_job.setter
    def workflow_job(self, value):
        raise ValueReadOnly

    @property
    def unified_job_template(self):
        """Unified job template"""
        return self._data.get("unified_job_template")

    @unified_job_template.setter
    def unified_job_template(self, value):
        raise ValueReadOnly

    @property
    def success_nodes(self):
        """Success nodes"""
        return self._data.get("success_nodes")

    @success_nodes.setter
    def success_nodes(self, value):
        raise ValueReadOnly

    @property
    def failure_nodes(self):
        """Failure nodes"""
        return self._data.get("failure_nodes")

    @failure_nodes.setter
    def failure_nodes(self, value):
        raise ValueReadOnly

    @property
    def always_nodes(self):
        """Always nodes"""
        return self._data.get("always_nodes")

    @always_nodes.setter
    def always_nodes(self, value):
        raise ValueReadOnly

    @property
    def all_parents_must_converge(self):
        """If enabled then the node will only run if all of the parent nodes have met the criteria to reach this 
        node"""
        return self._data.get("all_parents_must_converge")

    @all_parents_must_converge.setter
    def all_parents_must_converge(self, value):
        raise ValueReadOnly

    @property
    def do_not_run(self):
        """Indicates that a job will not be created when True. Workflow runtime semantics will mark this True if the 
        node is in a path that will decidedly not be ran. A value of False means the node may not run."""
        return self._data.get("do_not_run")

    @do_not_run.setter
    def do_not_run(self, value):
        raise ValueReadOnly

    @property
    def identifier(self):
        """An identifier coresponding to the workflow job template node that this node was created from."""
        return self._data.get("identifier")

    @identifier.setter
    def identifier(self, value):
        raise ValueReadOnly
