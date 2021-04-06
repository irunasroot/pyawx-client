from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class User(DataModelMixin):
    __endpoint__ = "/api/v2/users"

    def __init__(self, **kwargs):
        """
        User List

        Attributes:
            :param username: Required. 150 characters or fewer. Letters, digits and 
                @/./+/-/_ only.
            :type username: string, required, default ``
            :param first_name: First name
            :type first_name: string, required, default ``
            :param last_name: Last name
            :type last_name: string, required, default ``
            :param email: Email address
            :type email: string, required, default ``
            :param is_superuser: Designates that this user has all permissions without 
                explicitly assigning them.
            :type is_superuser: boolean, required, default False
            :param is_system_auditor: Is system auditor
            :type is_system_auditor: boolean, required, default False

        Read Only Attributes:
            :param id: Database ID for this user.
            :type id: integer, readonly
            :param type: Data type for this user.
                | user: User
            :type type: choice, readonly
            :param url: URL for this user.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this user was created.
            :type created: datetime, readonly
            :param ldap_dn: Ldap dn
            :type ldap_dn: string, readonly
            :param last_login: Last login
            :type last_login: datetime, readonly
            :param external_account: Set if the account is managed by an external service
            :type external_account: field, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this user."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this user."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this user."""
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
        """Timestamp when this user was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def username(self):
        """Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."""
        return self._data.get("username")

    @username.setter
    def username(self, value):
        set_changes(self, "username", value, types.STRING)

    @property
    def first_name(self):
        """First name"""
        return self._data.get("first_name")

    @first_name.setter
    def first_name(self, value):
        set_changes(self, "first_name", value, types.STRING)

    @property
    def last_name(self):
        """Last name"""
        return self._data.get("last_name")

    @last_name.setter
    def last_name(self, value):
        set_changes(self, "last_name", value, types.STRING)

    @property
    def email(self):
        """Email address"""
        return self._data.get("email")

    @email.setter
    def email(self, value):
        set_changes(self, "email", value, types.STRING)

    @property
    def is_superuser(self):
        """Designates that this user has all permissions without explicitly assigning them."""
        return self._data.get("is_superuser")

    @is_superuser.setter
    def is_superuser(self, value):
        set_changes(self, "is_superuser", value, types.BOOLEAN)

    @property
    def is_system_auditor(self):
        """Is system auditor"""
        return self._data.get("is_system_auditor")

    @is_system_auditor.setter
    def is_system_auditor(self, value):
        set_changes(self, "is_system_auditor", value, types.BOOLEAN)

    @property
    def ldap_dn(self):
        """Ldap dn"""
        return self._data.get("ldap_dn")

    @ldap_dn.setter
    def ldap_dn(self, value):
        raise ValueReadOnly

    @property
    def last_login(self):
        """Last login"""
        return self._data.get("last_login")

    @last_login.setter
    def last_login(self, value):
        raise ValueReadOnly

    @property
    def external_account(self):
        """Set if the account is managed by an external service"""
        return self._data.get("external_account")

    @external_account.setter
    def external_account(self, value):
        raise ValueReadOnly


class Team(DataModelMixin):
    __endpoint__ = "/api/v2/teams"

    def __init__(self, **kwargs):
        """
        Team List

        Attributes:
            :param name: Name of this team.
            :type name: string, required, default ``
            :param description: Optional description of this team.
            :type description: string, required, default ""
            :param organization: Organization
            :type organization: id, required, default ``

        Read Only Attributes:
            :param id: Database ID for this team.
            :type id: integer, readonly
            :param type: Data type for this team.
                | team: Team
            :type type: choice, readonly
            :param url: URL for this team.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this team was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this team was last modified.
            :type modified: datetime, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this team."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this team."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this team."""
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
        """Timestamp when this team was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this team was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this team."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this team."""
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


class Role(DataModelMixin):
    __endpoint__ = "/api/v2/roles"

    def __init__(self, **kwargs):
        """
        Role List

        Read Only Attributes:
            :param id: Database ID for this role.
            :type id: integer, readonly
            :param type: Data type for this role.
                | role: Role
            :type type: choice, readonly
            :param url: URL for this role.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param name: Name of this role.
            :type name: field, readonly
            :param description: Optional description of this role.
            :type description: field, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this role."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this role."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this role."""
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
    def name(self):
        """Name of this role."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this role."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        raise ValueReadOnly
