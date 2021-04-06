from pyawx.models._mixins import DataModelMixin
from pyawx.models.utils import set_changes, types
from pyawx.exceptions import ValueReadOnly


class NotificationTemplate(DataModelMixin):
    __endpoint__ = "/api/v2/notification_templates"

    def __init__(self, **kwargs):
        """
        Notification Template List

        Attributes:
            :param name: Name of this notification template.
            :type name: string, required, default ``
            :param description: Optional description of this notification template.
            :type description: string, required, default ""
            :param organization: Organization
            :type organization: id, required, default ``
            :param notification_type: Notification type
                | email: Email
                | grafana: Grafana
                | irc: IRC
                | mattermost: Mattermost
                | pagerduty: Pagerduty
                | rocketchat: Rocket.Chat
                | slack: Slack
                | twilio: Twilio
                | webhook: Webhook
            :type notification_type: choice, required, default ``
            :param notification_configuration: Notification configuration
            :type notification_configuration: json, required, default "{}"
            :param messages: Optional custom messages for notification template.
            :type messages: json, required, default "{'started': None, 'success': None, 'error': None, 'workflow_approval': None}"

        Read Only Attributes:
            :param id: Database ID for this notification template.
            :type id: integer, readonly
            :param type: Data type for this notification template.
                | notification_template: Notification Template
            :type type: choice, readonly
            :param url: URL for this notification template.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this notification template was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this notification template was last 
                modified.
            :type modified: datetime, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this notification template."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this notification template."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this notification template."""
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
        """Timestamp when this notification template was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this notification template was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def name(self):
        """Name of this notification template."""
        return self._data.get("name")

    @name.setter
    def name(self, value):
        set_changes(self, "name", value, types.STRING)

    @property
    def description(self):
        """Optional description of this notification template."""
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
    def notification_type(self):
        """Notification type"""
        return self._data.get("notification_type")

    @notification_type.setter
    def notification_type(self, value):
        allowed_values = [
            "email",
            "grafana",
            "irc",
            "mattermost",
            "pagerduty",
            "rocketchat",
            "slack",
            "twilio",
            "webhook"
        ]
        set_changes(self, "notification_type", value, types.CHOICE, allowed_values)

    @property
    def notification_configuration(self):
        """Notification configuration"""
        return self._data.get("notification_configuration")

    @notification_configuration.setter
    def notification_configuration(self, value):
        set_changes(self, "notification_configuration", value, types.JSON)

    @property
    def messages(self):
        """Optional custom messages for notification template."""
        return self._data.get("messages")

    @messages.setter
    def messages(self, value):
        set_changes(self, "messages", value, types.JSON)


class Notification(DataModelMixin):
    __endpoint__ = "/api/v2/notifications"

    def __init__(self, **kwargs):
        """
        Notification List

        Read Only Attributes:
            :param id: Database ID for this notification.
            :type id: integer, readonly
            :param type: Data type for this notification.
                | notification: Notification
            :type type: choice, readonly
            :param url: URL for this notification.
            :type url: string, readonly
            :param related: Data structure with URLs of related resources.
            :type related: object, readonly
            :param summary_fields: Data structure with name/description for related resources. 
                 The output for some objects may be limited for performance
            :type summary_fields: object, readonly
            :param created: Timestamp when this notification was created.
            :type created: datetime, readonly
            :param modified: Timestamp when this notification was last modified.
            :type modified: datetime, readonly
            :param notification_template: Notification template
            :type notification_template: id, readonly
            :param error: Error
            :type error: string, readonly
            :param status: Status
                | pending: Pending
                | successful: Successful
                | failed: Failed
            :type status: choice, readonly
            :param notifications_sent: Notifications sent
            :type notifications_sent: integer, readonly
            :param notification_type: Notification type
                | email: Email
                | grafana: Grafana
                | irc: IRC
                | mattermost: Mattermost
                | pagerduty: Pagerduty
                | rocketchat: Rocket.Chat
                | slack: Slack
                | twilio: Twilio
                | webhook: Webhook
            :type notification_type: choice, readonly
            :param recipients: Recipients
            :type recipients: string, readonly
            :param subject: Subject
            :type subject: string, readonly
            :param body: Notification body
            :type body: json, readonly
        """
        super().__init__(**kwargs)
    
    @property
    def id(self):
        """Database ID for this notification."""
        return self._data.get("id")

    @id.setter
    def id(self, value):
        raise ValueReadOnly

    @property
    def type(self):
        """Data type for this notification."""
        return self._data.get("type")

    @type.setter
    def type(self, value):
        raise ValueReadOnly

    @property
    def url(self):
        """URL for this notification."""
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
        """Timestamp when this notification was created."""
        return self._data.get("created")

    @created.setter
    def created(self, value):
        raise ValueReadOnly

    @property
    def modified(self):
        """Timestamp when this notification was last modified."""
        return self._data.get("modified")

    @modified.setter
    def modified(self, value):
        raise ValueReadOnly

    @property
    def notification_template(self):
        """Notification template"""
        return self._data.get("notification_template")

    @notification_template.setter
    def notification_template(self, value):
        raise ValueReadOnly

    @property
    def error(self):
        """Error"""
        return self._data.get("error")

    @error.setter
    def error(self, value):
        raise ValueReadOnly

    @property
    def status(self):
        """Status"""
        return self._data.get("status")

    @status.setter
    def status(self, value):
        raise ValueReadOnly

    @property
    def notifications_sent(self):
        """Notifications sent"""
        return self._data.get("notifications_sent")

    @notifications_sent.setter
    def notifications_sent(self, value):
        raise ValueReadOnly

    @property
    def notification_type(self):
        """Notification type"""
        return self._data.get("notification_type")

    @notification_type.setter
    def notification_type(self, value):
        raise ValueReadOnly

    @property
    def recipients(self):
        """Recipients"""
        return self._data.get("recipients")

    @recipients.setter
    def recipients(self, value):
        raise ValueReadOnly

    @property
    def subject(self):
        """Subject"""
        return self._data.get("subject")

    @subject.setter
    def subject(self, value):
        raise ValueReadOnly

    @property
    def body(self):
        """Notification body"""
        return self._data.get("body")

    @body.setter
    def body(self, value):
        raise ValueReadOnly
