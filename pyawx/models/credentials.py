from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class Credential(DataModelMixin):
    __endpoint__ = "/api/v2/credentials"

    def __init__(self, **kwargs):
        """
        Credential List

        Attributes:
            :param name: Name of this credential.
            :type name: string, required, default ``
            :param description: Optional description of this credential.
            :type description: string, required, default ""
            :param organization: Organization
            :type organization: id, required, default "None"
            :param credential_type: Specify the type of credential you want to create. Refer to 
                the Ansible Tower documentation for details on each typ
            :type credential_type: id, required, default ``
            :param inputs: Enter inputs using either JSON or YAML syntax. Refer to the 
                Ansible Tower documentation for example syntax.
            :type inputs: json, required, default "{}"

        Read Only Attributes:
            :param id: Database ID for this credential.
            :type id: integer, readonly
            :param type: Data type for this credential.
                | credential: Credential
            :type type: choice, readonly
            :param url: URL for this credential.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this credential was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this credential was last modified.
            :type modified: datetime, readonly
            :param managed_by_tower: Managed by tower
            :type managed_by_tower: boolean, readonly
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
        """Data type for this credential."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this credential."""
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
        """Timestamp when this credential was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this credential was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this credential."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this credential."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def organization(self):
        """Organization"""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.ID)

    @property
    def credential_type(self):
        """Specify the type of credential you want to create. Refer to the Ansible Tower documentation for details 
        on each type."""
        return self._data.get("credential_type")

    @credential_type.setter
    def credential_type(self, value):
        set_changes(self, "credential_type", value, types.ID)

    @property
    def managed_by_tower(self):
        """Managed by tower"""
        return self._data.get("managed_by_tower")

    @managed_by_tower.setter
    def managed_by_tower(self, value):
        raise ValueReadOnly

    @property
    def inputs(self):
        """Enter inputs using either JSON or YAML syntax. Refer to the Ansible Tower documentation for example 
        syntax."""
        return self._data.get("inputs")

    @inputs.setter
    def inputs(self, value):
        set_changes(self, "inputs", value, types.JSON)

    @property
    def kind(self):
        """Kind"""
        return self._data.get("kind")

    @kind.setter
    def kind(self, value):
        raise ValueReadOnly

    @property
    def cloud(self):
        """Cloud"""
        return self._data.get("cloud")

    @cloud.setter
    def cloud(self, value):
        raise ValueReadOnly

    @property
    def kubernetes(self):
        """Kubernetes"""
        return self._data.get("kubernetes")

    @kubernetes.setter
    def kubernetes(self, value):
        raise ValueReadOnly


class CredentialType(DataModelMixin):
    __endpoint__ = "/api/v2/credential_types"

    def __init__(self, **kwargs):
        """
        Credential Type List

        Attributes:
            :param name: Name of this credential type.
            :type name: string, required, default ``
            :param description: Optional description of this credential type.
            :type description: string, required, default ""
            :param kind: Kind
                | ssh: Machine
                | vault: Vault
                | net: Network
                | scm: Source Control
                | cloud: Cloud
                | token: Personal Access Token
                | insights: Insights
                | external: External
                | kubernetes: Kubernetes
                | galaxy: Galaxy/Automation Hub
            :type kind: choice, required, default ``
            :param inputs: Enter inputs using either JSON or YAML syntax. Refer to the 
                Ansible Tower documentation for example syntax.
            :type inputs: json, required, default "{}"
            :param injectors: Enter injectors using either JSON or YAML syntax. Refer to 
                the Ansible Tower documentation for example syntax.
            :type injectors: json, required, default "{}"

        Read Only Attributes:
            :param id: Database ID for this credential type.
            :type id: integer, readonly
            :param type: Data type for this credential type.
                | credential_type: Credential Type
            :type type: choice, readonly
            :param url: URL for this credential type.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this credential type was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this credential type was last modified.
            :type modified: datetime, readonly
            :param namespace: Namespace
            :type namespace: string, readonly
            :param managed_by_tower: Managed by tower
            :type managed_by_tower: boolean, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this credential type."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this credential type."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this credential type."""
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
        """Timestamp when this credential type was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this credential type was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this credential type."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this credential type."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def kind(self):
        """Kind"""
        return self._data.get("kind")

    @kind.setter
    def kind(self, value):
        allowed_values = [
            "net",
            "cloud"
        ]
        set_changes(self, "kind", value, types.CHOICE, allowed_values)

    @property
    def namespace(self):
        """Namespace"""
        return self._data.get("namespace")

    @namespace.setter
    def namespace(self, value):
        raise ValueReadOnly

    @property
    def managed_by_tower(self):
        """Managed by tower"""
        return self._data.get("managed_by_tower")

    @managed_by_tower.setter
    def managed_by_tower(self, value):
        raise ValueReadOnly

    @property
    def inputs(self):
        """Enter inputs using either JSON or YAML syntax. Refer to the Ansible Tower documentation for example 
        syntax."""
        return self._data.get("inputs")

    @inputs.setter
    def inputs(self, value):
        set_changes(self, "inputs", value, types.JSON)

    @property
    def injectors(self):
        """Enter injectors using either JSON or YAML syntax. Refer to the Ansible Tower documentation for example 
        syntax."""
        return self._data.get("injectors")

    @injectors.setter
    def injectors(self, value):
        set_changes(self, "injectors", value, types.JSON)


class CredentialInputSource(DataModelMixin):
    __endpoint__ = "/api/v2/credential_input_sources"

    def __init__(self, **kwargs):
        """
        Credential Input Sources

        Attributes:
            :param description: Optional description of this credential input source.
            :type description: string, required, default ""
            :param input_field_name: Input field name
            :type input_field_name: string, required, default ``
            :param metadata: Metadata
            :type metadata: json, required, default "{}"
            :param target_credential: Target credential
            :type target_credential: id, required, default ``
            :param source_credential: Source credential
            :type source_credential: id, required, default ``

        Read Only Attributes:
            :param id: Database ID for this credential input source.
            :type id: integer, readonly
            :param type: Data type for this credential input source.
                | credential_input_source: Credential Input Source
            :type type: choice, readonly
            :param url: URL for this credential input source.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this credential input source was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this credential input source was last 
                modified.
            :type modified: datetime, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this credential input source."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this credential input source."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this credential input source."""
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
        """Timestamp when this credential input source was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this credential input source was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this credential input source."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def input_field_name(self):
        """Input field name"""
        return self._data.get("input_field_name")

    @input_field_name.setter
    def input_field_name(self, value):
        set_changes(self, "input_field_name", value, types.STRING)

    @property
    def metadata(self):
        """Metadata"""
        return self._data.get("metadata")

    @metadata.setter
    def metadata(self, value):
        set_changes(self, "metadata", value, types.JSON)

    @property
    def target_credential(self):
        """Target credential"""
        return self._data.get("target_credential")

    @target_credential.setter
    def target_credential(self, value):
        set_changes(self, "target_credential", value, types.ID)

    @property
    def source_credential(self):
        """Source credential"""
        return self._data.get("source_credential")

    @source_credential.setter
    def source_credential(self, value):
        set_changes(self, "source_credential", value, types.ID)
