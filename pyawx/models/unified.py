from pyawx.models._mixins import DataModelMixin
from pyawx.exceptions import ValueReadOnly


class UnifiedJobTemplate(DataModelMixin):
    __endpoint__ = "/api/v2/unified_job_templates"

    def __init__(self, **kwargs):
        """
        Unified Job Template List

        Read Only Attributes:
            :param id: Database ID for this unified job template.
            :type id: integer, readonly
            :param type: Data type for this unified job template.
                | project: Project
                | inventory_source: Inventory Source
                | job_template: Job Template
                | system_job_template: System Job Template
                | workflow_job_template: Workflow Template
            :type type: choice, readonly
            :param url: URL for this unified job template.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this unified job template was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this unified job template was last modified.
            :type modified: datetime, readonly
            :param name: Name of this unified job template.
            :type name: string, readonly
            :param description: Optional description of this unified job template.
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
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this unified job template."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this unified job template."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this unified job template."""
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
        """Timestamp when this unified job template was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this unified job template was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this unified job template."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this unified job template."""
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


class UnifiedJob(DataModelMixin):
    __endpoint__ = "/api/v2/unified_jobs"

    def __init__(self, **kwargs):
        """
        Unified Job List

        Read Only Attributes:
            :param id: Database ID for this unified job.
            :type id: integer, readonly
            :param type: Data type for this unified job.
                | project_update: SCM Update
                | inventory_update: Inventory Sync
                | job: Playbook Run
                | ad_hoc_command: Command
                | system_job: Management Job
                | workflow_job: Workflow Job
            :type type: choice, readonly
            :param url: URL for this unified job.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this unified job was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this unified job was last modified.
            :type modified: datetime, readonly
            :param name: Name of this unified job.
            :type name: string, readonly
            :param description: Optional description of this unified job.
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
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this unified job."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this unified job."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this unified job."""
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
        """Timestamp when this unified job was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this unified job was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this unified job."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this unified job."""
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
