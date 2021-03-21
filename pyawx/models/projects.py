from pyawx.models import types
from pyawx.models.mixins import DataModelMixin
from pyawx.models.utils import set_changes
from pyawx.exceptions import ValueReadOnly


class Project(DataModelMixin):
    __endpoint__ = "/api/v2/projects"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param name: Name of this project.
            :type name: str, required
            :param description: Optional description of this project.
            :type description: str, default ""
            :param local_path: Local path (relative to PROJECTS_ROOT) containing playbooks and
                related files for this project.
            :type local_path: str, default ""
            :param scm_type: Specifies the source control system used to store the project.
                | "": Manual
                | git: Git
                | hg: Mercurial
                | svn: Subversion
                | insights: Red Hat Insights
                | archive: Remote Archive
            :type scm_type: str, choice, default ""
            :param scm_url: The location where the project is stored.
            :type scm_url: str, default ""
            :param scm_branch: Specific branch, tag or commit to checkout.
            :type scm_branch: str, default ""
            :param scm_refspec: For git projects, an additional refspec to fetch.
            :type scm_refspec: str, default ""
            :param scm_clean: Discard any local changes before syncing the project.
            :type scm_clean: bool, default False
            :param scm_delete_on_update: Delete the project before syncing.
            :type scm_delete_on_update: bool, default False
            :param scm_update_cache_timeout: The number of seconds after the last project update ran that a new
                project update will be launched as a job dependency.
            :type scm_update_cache_timeout: int, default 0
            :param allow_override: Allow changing the SCM branch or revision in a job template that uses this project.
            :type allow_override: bool, default False
            :param credential: "Credential ID (id)"
            :type credential: str, default ""
            :param timeout: The amount of time (in seconds) to run before the task is canceled.
            :type timeout: int, default 0
            :param organization: The organization used to determine access to this template.
            :type organization: str, default ""
            :param scm_update_on_launch: Update the project when a job is launched that uses the project.
            :type scm_update_on_launch: bool, default False
            :param custom_virtualenv: Local absolute file path containing a custom Python virtualenv to use
            :type custom_virtualenv: str, default ""

        Read Only Attributes:
            :param id: Database ID for this project.
            :type id: int, readonly
            :param type: Data type for this project.
            :type type: str, readonly
            :param url: URL for this project.
            :type url: str, readonly
            :param created: Timestamp when this project was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this project was last modified.
            :type modified: datetime, readonly
            :param last_job_run: Last time job ran
            :type last_job_run: datetime, readonly
            :param last_job_failed: If last job failed or not
            :type last_job_failed: bool, readonly
            :param next_job_run: Next time job is going to run
            :type next_job_run: datetime, readonly
            :param last_update_failed: If the last update failed
            :type last_update_failed: bool, readonly
            :param last_updated: When the last update happened
            :type last_updated: datetime, readonly
            :param scm_revision: The last revision fetched by a project update
            :type scm_revision: str, readonly
            :param status: Status of the current running/last job
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
            :type status: str, choice, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this project. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this project. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this project. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this project was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this project was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this project. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this project. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def local_path(self):
        """Local path (relative to PROJECTS_ROOT) containing playbooks and related files for this project. (string)"""
        return self._data.get("local_path")

    @local_path.setter
    def local_path(self, value):
        raise ValueReadOnly

    @property
    def scm_type(self):
        """Specifies the source control system used to store the project. (choice)"""
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
        set_changes(self, "scm_type", value, types.STRING, allowed_values)

    @property
    def scm_url(self):
        """The location where the project is stored. (string)"""
        return self._data.get("scm_url")

    @scm_url.setter
    def scm_url(self, value):
        set_changes(self, "scm_url", value, types.STRING)

    @property
    def scm_branch(self):
        """Specific branch, tag or commit to checkout. (string)"""
        return self._data.get("scm_branch")

    @scm_branch.setter
    def scm_branch(self, value):
        set_changes(self, "scm_branch", value, types.STRING)

    @property
    def scm_refspec(self):
        """For git projects, an additional refspec to fetch. (string)"""
        return self._data.get("scm_refspec")

    @scm_refspec.setter
    def scm_refspec(self, value):
        set_changes(self, "scm_refspec", value, types.STRING)

    @property
    def scm_clean(self):
        """Discard any local changes before syncing the project. (boolean)"""
        return self._data.get("scm_clean")

    @scm_clean.setter
    def scm_clean(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "scm_clean", value, types.BOOLEAN, allowed_values)

    @property
    def scm_delete_on_update(self):
        """Delete the project before syncing. (boolean)"""
        return self._data.get("scm_delete_on_update")

    @scm_delete_on_update.setter
    def scm_delete_on_update(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "scm_delete_on_update", value, types.BOOLEAN, allowed_values)

    @property
    def scm_revision(self):
        """The last revision fetched by a project update (string)"""
        return self._data.get("scm_revision")

    @scm_revision.setter
    def scm_revision(self, value):
        raise ValueReadOnly

    @property
    def scm_update_on_launch(self):
        """Update the project when a job is launched that uses the project. (boolean)"""
        return self._data.get("scm_update_on_launch")

    @scm_update_on_launch.setter
    def scm_update_on_launch(self, value):
        allowed_types = [
            True,
            False
        ]
        set_changes(self, "scm_update_on_launch", value, types.BOOLEAN, allowed_types)

    @property
    def scm_update_cache_timeout(self):
        """
        The number of seconds after the last project update ran that a new project
        update will be launched as a job dependency. (integer)
        """
        return self._data.get("scm_update_cache_timeout")

    @scm_update_cache_timeout.setter
    def scm_update_cache_timeout(self, value):
        set_changes(self, "scm_update_cache_timeout", value, types.INTEGER)

    @property
    def credential(self):
        """Credential ID (id)"""
        return self._data.get("credential")

    @credential.setter
    def credential(self, value):
        set_changes(self, "timeout", value, types.STRING)

    @property
    def timeout(self):
        """The amount of time (in seconds) to run before the task is canceled. (integer)"""
        return self._data.get("timeout")

    @timeout.setter
    def timeout(self, value):
        set_changes(self, "timeout", value, types.INTEGER)

    @property
    def last_job_run(self):
        """Last time job ran (datetime)"""
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
        """Next job run (datetime)"""
        return self._data.get("next_job_run")

    @next_job_run.setter
    def next_job_run(self, value):
        raise ValueReadOnly

    @property
    def status(self):
        """Status of job (string)"""
        return self._data.get("status")

    @status.setter
    def status(self, value):
        raise ValueReadOnly

    @property
    def organization(self):
        """The organization used to determine access to this template. (id)"""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        raise ValueReadOnly

    @property
    def allow_override(self):
        """Allow changing the SCM branch or revision in a job template that uses this project. (boolean)"""
        return self._data.get("allow_override")

    @allow_override.setter
    def allow_override(self, value):
        allowed_types = [
            True,
            False
        ]
        set_changes(self, "allow_override", value, types.BOOLEAN, allowed_types)

    @property
    def custom_virtualenv(self):
        """Local absolute file path containing a custom Python virtualenv to use (string)"""
        return self._data.get("custom_virtualenv")

    @custom_virtualenv.setter
    def custom_virtualenv(self, value):
        raise ValueReadOnly

    @property
    def last_update_failed(self):
        """Last update failed (boolean)"""
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
