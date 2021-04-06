from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class Project(DataModelMixin):
    __endpoint__ = "/api/v2/projects"

    def __init__(self, **kwargs):
        """
        Project List

        Attributes:
            :param name: Name of this project.
            :type name: string, required, default ``
            :param description: Optional description of this project.
            :type description: string, required, default ""
            :param local_path: Local path (relative to PROJECTS_ROOT) containing playbooks 
                and related files for this project.
            :type local_path: string, required, default ``
            :param scm_type: Specifies the source control system used to store the 
                project.
                | : Manual
                | git: Git
                | hg: Mercurial
                | svn: Subversion
                | insights: Red Hat Insights
                | archive: Remote Archive
            :type scm_type: choice, required, default ""
            :param scm_url: The location where the project is stored.
            :type scm_url: string, required, default ""
            :param scm_branch: Specific branch, tag or commit to checkout.
            :type scm_branch: string, required, default ""
            :param scm_refspec: For git projects, an additional refspec to fetch.
            :type scm_refspec: string, required, default ""
            :param scm_clean: Discard any local changes before syncing the project.
            :type scm_clean: boolean, required, default False
            :param scm_delete_on_update: Delete the project before syncing.
            :type scm_delete_on_update: boolean, required, default False
            :param credential: Credential
            :type credential: id, required, default ``
            :param timeout: The amount of time (in seconds) to run before the task is 
                canceled.
            :type timeout: integer, required, default 0
            :param organization: The organization used to determine access to this template.
            :type organization: id, required, default ``
            :param scm_update_on_launch: Update the project when a job is launched that uses the 
                project.
            :type scm_update_on_launch: boolean, required, default False
            :param scm_update_cache_timeout: The number of seconds after the last project update ran 
                that a new project update will be launched as a job
            :type scm_update_cache_timeout: integer, required, default 0
            :param allow_override: Allow changing the SCM branch or revision in a job template 
                that uses this project.
            :type allow_override: boolean, required, default False
            :param custom_virtualenv: Local absolute file path containing a custom Python 
                virtualenv to use
            :type custom_virtualenv: string, required, default "None"

        Read Only Attributes:
            :param id: Database ID for this project.
            :type id: integer, readonly
            :param type: Data type for this project.
                | project: Project
            :type type: choice, readonly
            :param url: URL for this project.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this project was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this project was last modified.
            :type modified: datetime, readonly
            :param scm_revision: The last revision fetched by a project update
            :type scm_revision: string, readonly
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
            :type status: choice, readonly
            :param last_update_failed: Last update failed
            :type last_update_failed: boolean, readonly
            :param last_updated: Last updated
            :type last_updated: datetime, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this project."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this project."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this project."""
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
        """Timestamp when this project was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this project was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this project."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this project."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def local_path(self):
        """Local path (relative to PROJECTS_ROOT) containing playbooks and related files for this project."""
        return self._data.get("local_path")

    @local_path.setter
    def local_path(self, value):
        set_changes(self, "local_path", value, types.STRING)

    @property
    def scm_type(self):
        """Specifies the source control system used to store the project."""
        return self._data.get("scm_type")

    @scm_type.setter
    def scm_type(self, value):
        allowed_values = [
            "",
            "git",
            "hg",
            "svn",
            "insights",
            "archive"
        ]
        set_changes(self, "scm_type", value, types.CHOICE, allowed_values)

    @property
    def scm_url(self):
        """The location where the project is stored."""
        return self._data.get("scm_url")

    @scm_url.setter
    def scm_url(self, value):
        set_changes(self, "scm_url", value, types.STRING)

    @property
    def scm_branch(self):
        """Specific branch, tag or commit to checkout."""
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
        set_changes(self, "scm_branch", value, types.STRING)

    @property
    def scm_refspec(self):
        """For git projects, an additional refspec to fetch."""
        return self._data.get("scm_refspec")

    @scm_refspec.setter
    def scm_refspec(self, value):
        set_changes(self, "scm_refspec", value, types.STRING)

    @property
    def scm_clean(self):
        """Discard any local changes before syncing the project."""
        return self._data.get("scm_clean")

    @scm_clean.setter
    def scm_clean(self, value):
        set_changes(self, "scm_clean", value, types.BOOLEAN)

    @property
    def scm_delete_on_update(self):
        """Delete the project before syncing."""
        return self._data.get("scm_delete_on_update")

    @scm_delete_on_update.setter
    def scm_delete_on_update(self, value):
        set_changes(self, "scm_delete_on_update", value, types.BOOLEAN)

    @property
    def credential(self):
        """Credential"""
        return self._data.get("credential")

    @credential.setter
    def credential(self, value):
        set_changes(self, "credential", value, types.ID)

    @property
    def timeout(self):
        """The amount of time (in seconds) to run before the task is canceled."""
        return self._data.get("timeout")

    @timeout.setter
    def timeout(self, value):
        set_changes(self, "timeout", value, types.INTEGER)

    @property
    def scm_revision(self):
        """The last revision fetched by a project update"""
        return self._data.get("scm_revision")

    @scm_revision.setter
    def scm_revision(self, value):
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
    def organization(self):
        """The organization used to determine access to this template."""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.ID)

    @property
    def scm_update_on_launch(self):
        """Update the project when a job is launched that uses the project."""
        return self._data.get("scm_update_on_launch")

    @scm_update_on_launch.setter
    def scm_update_on_launch(self, value):
        set_changes(self, "scm_update_on_launch", value, types.BOOLEAN)

    @property
    def scm_update_cache_timeout(self):
        """The number of seconds after the last project update ran that a new project update will be launched as a 
        job dependency."""
        return self._data.get("scm_update_cache_timeout")

    @scm_update_cache_timeout.setter
    def scm_update_cache_timeout(self, value):
        set_changes(self, "scm_update_cache_timeout", value, types.INTEGER)

    @property
    def allow_override(self):
        """Allow changing the SCM branch or revision in a job template that uses this project."""
        return self._data.get("allow_override")

    @allow_override.setter
    def allow_override(self, value):
        set_changes(self, "allow_override", value, types.BOOLEAN)

    @property
    def custom_virtualenv(self):
        """Local absolute file path containing a custom Python virtualenv to use"""
        return self._data.get("custom_virtualenv")

    @custom_virtualenv.setter
    def custom_virtualenv(self, value):
        set_changes(self, "custom_virtualenv", value, types.STRING)

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


class ProjectUpdate(DataModelMixin):
    __endpoint__ = "/api/v2/project_updates"

    def __init__(self, **kwargs):
        """
        Project Update List

        Read Only Attributes:
            :param id: Database ID for this project update.
            :type id: integer, readonly
            :param type: Data type for this project update.
                | project_update: SCM Update
            :type type: choice, readonly
            :param url: URL for this project update.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this project update was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this project update was last modified.
            :type modified: datetime, readonly
            :param name: Name of this project update.
            :type name: string, readonly
            :param description: Optional description of this project update.
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
            :param local_path: Local path (relative to PROJECTS_ROOT) containing playbooks 
                and related files for this project.
            :type local_path: string, readonly
            :param scm_type: Specifies the source control system used to store the 
                project.
                | : Manual
                | git: Git
                | hg: Mercurial
                | svn: Subversion
                | insights: Red Hat Insights
                | archive: Remote Archive
            :type scm_type: choice, readonly
            :param scm_url: The location where the project is stored.
            :type scm_url: string, readonly
            :param scm_branch: Specific branch, tag or commit to checkout.
            :type scm_branch: string, readonly
            :param scm_refspec: For git projects, an additional refspec to fetch.
            :type scm_refspec: string, readonly
            :param scm_clean: Discard any local changes before syncing the project.
            :type scm_clean: boolean, readonly
            :param scm_delete_on_update: Delete the project before syncing.
            :type scm_delete_on_update: boolean, readonly
            :param credential: Credential
            :type credential: id, readonly
            :param timeout: The amount of time (in seconds) to run before the task is 
                canceled.
            :type timeout: integer, readonly
            :param scm_revision: The SCM Revision discovered by this update for the given 
                project and branch.
            :type scm_revision: string, readonly
            :param project: Project
            :type project: id, readonly
            :param job_type: Job type
                | run: Run
                | check: Check
            :type job_type: choice, readonly
            :param job_tags: Parts of the project update playbook that will be run.
            :type job_tags: string, readonly
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
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this project update."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this project update."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this project update."""
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
        """Timestamp when this project update was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this project update was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this project update."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this project update."""
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
    def local_path(self):
        """Local path (relative to PROJECTS_ROOT) containing playbooks and related files for this project."""
        return self._data.get("local_path")

    @local_path.setter
    def local_path(self, value):
        raise ValueReadOnly

    @property
    def scm_type(self):
        """Specifies the source control system used to store the project."""
        return self._data.get("scm_type")

    @scm_type.setter
    def scm_type(self, value):
        raise ValueReadOnly

    @property
    def scm_url(self):
        """The location where the project is stored."""
        return self._data.get("scm_url")

    @scm_url.setter
    def scm_url(self, value):
        raise ValueReadOnly

    @property
    def scm_branch(self):
        """Specific branch, tag or commit to checkout."""
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
        raise ValueReadOnly

    @property
    def scm_refspec(self):
        """For git projects, an additional refspec to fetch."""
        return self._data.get("scm_refspec")

    @scm_refspec.setter
    def scm_refspec(self, value):
        raise ValueReadOnly

    @property
    def scm_clean(self):
        """Discard any local changes before syncing the project."""
        return self._data.get("scm_clean")

    @scm_clean.setter
    def scm_clean(self, value):
        raise ValueReadOnly

    @property
    def scm_delete_on_update(self):
        """Delete the project before syncing."""
        return self._data.get("scm_delete_on_update")

    @scm_delete_on_update.setter
    def scm_delete_on_update(self, value):
        raise ValueReadOnly

    @property
    def credential(self):
        """Credential"""
        return self._data.get("credential")

    @credential.setter
    def credential(self, value):
        raise ValueReadOnly

    @property
    def timeout(self):
        """The amount of time (in seconds) to run before the task is canceled."""
        return self._data.get("timeout")

    @timeout.setter
    def timeout(self, value):
        raise ValueReadOnly

    @property
    def scm_revision(self):
        """The SCM Revision discovered by this update for the given project and branch."""
        return self._data.get("scm_revision")

    @scm_revision.setter
    def scm_revision(self, value):
        raise ValueReadOnly

    @property
    def project(self):
        """Project"""
        return self._data.get("project")

    @project.setter
    def project(self, value):
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
        """Parts of the project update playbook that will be run."""
        return self._data.get("job_tags")

    @job_tags.setter
    def job_tags(self, value):
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
