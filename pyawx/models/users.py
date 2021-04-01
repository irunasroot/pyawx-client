from pyawx.models import types
from pyawx.models.mixins import DataModelMixin
from pyawx.models.utils import set_changes
from pyawx.exceptions import ValueReadOnly


class User(DataModelMixin):
    __endpoint__ = "/api/v2/users"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param username: Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
            :type username: str, required
            :param first_name: First name
            :type first_name: str, default ""
            :param last_name: Last name
            :type last_name: str, default ""
            :param email: Email
            :type email: str, default ""
            :param is_superuser: Designates that this user has all permissions without explicitly assigning them.
            :type is_superuser: bool, default False

        Write Only Attributes
            :param password: Write-only field used to change the password. (string, default="")
            :type password: str, writeonly

        Read Only Attributes:
            :param id: Database ID for this user.
            :type id: int, readonly
            :param type: Data type for this user.
            :type type: str, readonly
            :param url: URL for this user.
            :type url: str, readonly
            :param created: Timestamp when this user was created.
            :type created: datetime, readonly
            :param ldap_dn: LDAP dn
            :type ldap_dn: str, readonly
            :param last_login: Last login
            :type last_login: datetime, readonly
            :param external_account: Set if the account is managed by an external service
            :type external_account: str, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this user. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this user. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this user. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this user was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def username(self):
        """Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. (string)"""
        return self._data.get("username")

    @username.setter
    def username(self, value):
        set_changes(self, "username", value, types.STRING)

    @property
    def first_name(self):
        """Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. (string)"""
        return self._data.get("first_name")

    @first_name.setter
    def first_name(self, value):
        set_changes(self, "first_name", value, types.STRING)

    @property
    def last_name(self):
        """Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. (string)"""
        return self._data.get("last_name")

    @last_name.setter
    def last_name(self, value):
        set_changes(self, "last_name", value, types.STRING)

    @property
    def email(self):
        """Email"""
        return self._data.get("email")

    @email.setter
    def email(self, value):
        set_changes(self, "email", value, types.STRING)

    @property
    def is_superuser(self):
        """Designates that this user has all permissions without explicitly assigning them. (boolean)"""
        return self._data.get("is_superuser")

    @is_superuser.setter
    def is_superuser(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "is_superuser", value, types.BOOLEAN, allowed_values)

    @property
    def is_system_auditor(self):
        """User is system auditor (boolean)"""
        return self._data.get("is_system_auditor")

    @is_system_auditor.setter
    def is_system_auditor(self, value):
        allowed_values = [
            True,
            False
        ]
        set_changes(self, "is_system_auditor", value, types.BOOLEAN, allowed_values)

    @property
    def ldap_dn(self):
        """Designates that this user has all permissions without explicitly assigning them. (boolean)"""
        return self._data.get("ldap_dn")

    @ldap_dn.setter
    def ldap_dn(self, value):
        raise ValueReadOnly

    @property
    def last_login(self):
        """Last login (datetime)"""
        return self._data.get("last_login")

    @last_login.setter
    def last_login(self, value):
        raise ValueReadOnly

    @property
    def external_account(self):
        """Set if the account is managed by an external service (field)"""
        return self._data.get("external_account")

    @external_account.setter
    def external_account(self, value):
        raise ValueReadOnly

    @property
    def password(self):
        """Write-only field used to change the password. (string)"""
        return self._data.get("password")

    @password.setter
    def password(self, value):
        set_changes(self, "password", value, types.STRING)


class Team(DataModelMixin):
    __endpoint__ = "/api/v2/teams"

    def __init__(self, **kwargs):
        """
        Attributes:
            :param name: Name of this team
            :type name: str, required
            :param description: Optional description of this team. (string)
            :type description: str, default ""
            :param organization: Optional description of this team. (string)
            :type organization: int, required

        Read Only Attributes:
            :param id: Database ID for this team.
            :type id: int, readonly
            :param type: Data type for this team.
            :type type: str, readonly
            :param url: URL for this team.
            :type url: str, readonly
            :param created: Timestamp when this team was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this team was last modified.
            :type modified: datetime, readonly
        """
        super().__init__(**kwargs)

    @property
    def id(self):
        """Database ID for this team. (integer)"""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this team. (choice)"""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this team. (string)"""
        return self._data.get("url")

    @url.setter
    def url(self, value):
        raise ValueReadOnly

    @property
    def created(self):
        """Timestamp when this team was created. (datetime)"""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this team was last modified. (datetime)"""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this team. (string)"""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this team. (string)"""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def organization(self):
        """Optional description of this team. (string)"""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.INTEGER)
