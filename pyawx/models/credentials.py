from pyawx.models import types
from pyawx.models.mixins import DataModelMixin
from pyawx.models.utils import set_changes
from pyawx.exceptions import ValueReadOnly


class Credential(DataModelMixin):
    __endpoint__ = "/api/v2/credentials"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param name: Name of this credential.
            :type name: str, required
            :param description: Optional description of this credential
            :type description: str, default ""
            :param organization: Inherit permissions from organization roles.
                If provided on creation, do not give either user or team.
            :type organization: int, Default None
            :param credential_type: Specify the type of credential you want to create.
            :type credential_type: int, required
            :param inputs: Enter inputs using either JSON syntax.
            :type inputs: json, default {}

        Write Only Attributes:
            :param user: Write-only field used to add user to owner role.
                If provided, do not give either team or organization. Only valid for creation.
            :type user: int, Default None
            :param team: Write-only field used to add team to owner role.
                If provided, do not give either user or organization. Only valid for creation.

        Read Only Attributes:
            :param id: Database ID for this credential.
            :type id: int, readonly
            :param type: Data type for this credential.
            :type type: str, readonly
            :param url: URL for this credential. (string)
            :type url: str, readonly
            :param created: Timestamp when this credential was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this credential was last modified.
            :type modified: datetime, readonly
            :param managed_by_tower: Managed by Tower
            :type managed_by_tower: bool, readonly
            :param kind: Kind
            :type kind: field, readonly
            :param cloud: Cloud
            :type cloud: field, readonly
            :param kubernetes: Kubernetes
            :type kubernetes: field, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this credential."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this credential. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this credential. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this credential was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this credential was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this credential. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this credential. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def organization(self):
        """
        Inherit permissions from organization roles.
        If provided on creation, do not give either user or team. (id)
        """
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.INTEGER)

    @property
    def credential_type(self):
        """Specify the type of credential you want to create. (id)"""
        return self._data.get("credential_type")

    @credential_type.setter
    def credential_type(self, value):
        set_changes(self, "credential_type", value, types.INTEGER)

    @property
    def managed_by_tower(self):
        """Managed by Tower (boolean)"""
        return self._data.get("managed_by_tower")

    @managed_by_tower.setter
    def managed_by_tower(self, value):
        raise ValueReadOnly

    @property
    def inputs(self):
        """Enter inputs using either JSON syntax. (json)"""
        return self._data.get("inputs")

    @inputs.setter
    def inputs(self, value):
        set_changes(self, "inputs", value, types.STRING)

    @property
    def kind(self):
        """Kind (field)"""
        return self._data.get("kind")

    @kind.setter
    def kind(self, value):
        set_changes(self, "kind", value, types.STRING)

    @property
    def cloud(self):
        """Cloud (field)"""
        return self._data.get("cloud")

    @cloud.setter
    def cloud(self, value):
        set_changes(self, "cloud", value, types.STRING)

    @property
    def kubernetes(self):
        """Kubernetes (field)"""
        return self._data.get("kubernetes")

    @kubernetes.setter
    def kubernetes(self, value):
        set_changes(self, "kubernetes", value, types.STRING)

    @property
    def user(self):
        """
        Write-only field used to add user to owner role. If provided, do not give either team or organization.
        Only valid for creation.
        """
        return self._data.get("user")

    @user.setter
    def user(self, value):
        set_changes(self, "user", value, types.INTEGER)

    @property
    def team(self):
        """
        Write-only field used to add team to owner role.
        If provided, do not give either user or organization. Only valid for creation. (id, default=None)
        """
        return self._data.get("team")

    @team.setter
    def team(self, value):
        set_changes(self, "team", value, types.INTEGER)


class CredentialType(DataModelMixin):
    __endpoint__ = "/api/v2/credential_types"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param name: Name of this credential type.
            :type name: str, required
            :param description: Optional description of this credential type.
            :type description: str, default ""
            :param kind: Kind of  credential type.
            :type kind: choice, str, required
                | net: Network
                | cloud: Cloud
            :param inputs: Enter inputs using JSON.
            :type inputs: json, Default {}
            :param injectors: Enter injectors using JSON.
            :type injectors: json, Default {}

        Read Only Attributes:
            :param id: Database ID for this credential type
            :type id: int, readonly
            :param type: Data type for this credential type.
            :type type: str, readonly
            :param url: URL for this credential type.
            :type url: str, readonly
            :param created: Timestamp when this credential type was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this credential type was last modified.
            :type modified: datetime, readonly
            :param kind: Kind of  credential type.
            :type kind: choice, str, required
                | ssh: Machine
                | vault: Vault
                | scm: Source Control
                | token: Personal Access Token
                | insights: Insights
                | external: External
                | kubernetes: Kubernetes
                | galaxy: Galaxy/Automation Hub
            :param namespace: Namespace
            :type namesapce: str, readonly
            :param managed_by_tower: Managed by Tower
            :type managed_by_tower: bool, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this credential type. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this credential type. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this credential type. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this credential type was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this credential type was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this credential type. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this credential type. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def kind(self):
        """Kind of  credential type. (choice)"""
        return self._data.get("kind")

    @kind.setter
    def kind(self, value):
        allowed_values = [
            "net",
            "cloud"
        ]
        set_changes(self, "kind", value, types.STRING, allowed_values)

    @property
    def namespace(self):
        """Namesapce (string)"""
        return self._data.get("namespace")

    @namespace.setter
    def namespace(self, value):
        raise ValueReadOnly

    @property
    def managed_by_tower(self):
        """Managed by Tower (boolean)"""
        return self._data.get("managed_by_tower")

    @managed_by_tower.setter
    def managed_by_tower(self, value):
        raise ValueReadOnly

    @property
    def inputs(self):
        """ Enter inputs using JSON syntax. (json)"""
        return self._data.get("inputs")

    @inputs.setter
    def inputs(self, value):
        set_changes(self, "inputs", value, types.JSON)

    @property
    def injectors(self):
        """Enter injectors using JSON syntax. (json)"""
        return self._data.get("injectors")

    @injectors.setter
    def injectors(self, value):
        set_changes(self, "injectors", value, types.JSON)
