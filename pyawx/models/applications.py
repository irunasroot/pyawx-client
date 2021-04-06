from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class Application(DataModelMixin):
    __endpoint__ = "/api/v2/applications"

    def __init__(self, **kwargs):
        """
        OAuth 2 Applications

        Attributes:
            :param name: Name of this application.
            :type name: string, required, default ``
            :param description: Optional description of this application.
            :type description: string, required, default ""
            :param client_type: Set to Public or Confidential depending on how secure the 
                client device is.
                | confidential: Confidential
                | public: Public
            :type client_type: choice, required, default ``
            :param redirect_uris: Allowed URIs list, space separated
            :type redirect_uris: string, required, default ``
            :param authorization_grant_type: The Grant type the user must use for acquire tokens for 
                this application.
                | authorization-code: Authorization code
                | password: Resource owner password-based
            :type authorization_grant_type: choice, required, default ``
            :param skip_authorization: Set True to skip authorization step for completely trusted 
                applications.
            :type skip_authorization: boolean, required, default False
            :param organization: Organization containing this application.
            :type organization: id, required, default ``

        Read Only Attributes:
            :param id: Database ID for this application.
            :type id: integer, readonly
            :param type: Data type for this application.
                | o_auth2_application: Application
            :type type: choice, readonly
            :param url: URL for this application.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this application was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this application was last modified.
            :type modified: datetime, readonly
            :param client_id: Client id
            :type client_id: string, readonly
            :param client_secret: Used for more stringent verification of access to an 
                application when creating a token.
            :type client_secret: string, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this application."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this application."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this application."""
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
        """Timestamp when this application was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this application was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this application."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this application."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def client_id(self):
        """Client id"""
        return self._data.get("client_id")

    @client_id.setter
    def client_id(self, value):
        raise ValueReadOnly

    @property
    def client_secret(self):
        """Used for more stringent verification of access to an application when creating a token."""
        return self._data.get("client_secret")

    @client_secret.setter
    def client_secret(self, value):
        raise ValueReadOnly

    @property
    def client_type(self):
        """Set to Public or Confidential depending on how secure the client device is."""
        return self._data.get("client_type")

    @client_type.setter
    def client_type(self, value):
        allowed_values = [
            "confidential",
            "public"
        ]
        set_changes(self, "client_type", value, types.CHOICE, allowed_values)

    @property
    def redirect_uris(self):
        """Allowed URIs list, space separated"""
        return self._data.get("redirect_uris")

    @redirect_uris.setter
    def redirect_uris(self, value):
        set_changes(self, "redirect_uris", value, types.STRING)

    @property
    def authorization_grant_type(self):
        """The Grant type the user must use for acquire tokens for this application."""
        return self._data.get("authorization_grant_type")

    @authorization_grant_type.setter
    def authorization_grant_type(self, value):
        allowed_values = [
            "authorization-code",
            "password"
        ]
        set_changes(self, "authorization_grant_type", value, types.CHOICE, allowed_values)

    @property
    def skip_authorization(self):
        """Set True to skip authorization step for completely trusted applications."""
        return self._data.get("skip_authorization")

    @skip_authorization.setter
    def skip_authorization(self, value):
        set_changes(self, "skip_authorization", value, types.BOOLEAN)

    @property
    def organization(self):
        """Organization containing this application."""
        return self._data.get("organization")

    @organization.setter
    def organization(self, value):
        set_changes(self, "organization", value, types.ID)


class Token(DataModelMixin):
    __endpoint__ = "/api/v2/tokens"

    def __init__(self, **kwargs):
        """
        OAuth2 Tokens

        Attributes:
            :param description: Optional description of this access token.
            :type description: string, required, default ""
            :param application: Application
            :type application: id, required, default ``
            :param scope: Allowed scopes, further restricts user's permissions. Must 
                be a simple space-separated string with allowed scopes
            :type scope: string, required, default "write"

        Read Only Attributes:
            :param id: Database ID for this access token.
            :type id: integer, readonly
            :param type: Data type for this access token.
                | o_auth2_access_token: Access Token
            :type type: choice, readonly
            :param url: URL for this access token.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this access token was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this access token was last modified.
            :type modified: datetime, readonly
            :param user: The user representing the token owner
            :type user: id, readonly
            :param token: Token
            :type token: string, readonly
            :param refresh_token: Refresh token
            :type refresh_token: field, readonly
            :param expires: Expires
            :type expires: datetime, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this access token."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this access token."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this access token."""
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
        """Timestamp when this access token was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this access token was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def description(self):
        """Optional description of this access token."""
        return self._data.get("description")

    @description.setter
    def description(self, value):
        set_changes(self, "description", value, types.STRING)

    @property
    def user(self):
        """The user representing the token owner"""
        return self._data.get("user")

    @user.setter
    def user(self, value):
        raise ValueReadOnly

    @property
    def token(self):
        """Token"""
        return self._data.get("token")

    @token.setter
    def token(self, value):
        raise ValueReadOnly

    @property
    def refresh_token(self):
        """Refresh token"""
        return self._data.get("refresh_token")

    @refresh_token.setter
    def refresh_token(self, value):
        raise ValueReadOnly

    @property
    def application(self):
        """Application"""
        return self._data.get("application")

    @application.setter
    def application(self, value):
        set_changes(self, "application", value, types.ID)

    @property
    def expires(self):
        """Expires"""
        return self._data.get("expires")

    @expires.setter
    def expires(self, value):
        raise ValueReadOnly

    @property
    def scope(self):
        """Allowed scopes, further restricts user's permissions. Must be a simple space-separated string with 
        allowed scopes ['read', 'write']."""
        return self._data.get("scope")

    @scope.setter
    def scope(self, value):
        set_changes(self, "scope", value, types.STRING)
