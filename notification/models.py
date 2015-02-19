from django.db import models
from django.utils import timezone


class Email(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email


class Client(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(
        max_length=255,
        help_text="Use format: Country/City as used by pytz")
    emails = models.ManyToManyField(Email)

    def __unicode__(self):
        return self.name


class NotificationType(models.Model):
    notification_type = models.CharField(max_length=255)
    colour = models.CharField(max_length=255)

    def __unicode__(self):
        return self.notification_type


class Notification(models.Model):
    client = models.ForeignKey(Client)
    ntype = models.ForeignKey(NotificationType)
    headline = models.CharField(max_length=255)
    ticket = models.CharField(max_length=255)
    raised = models.DateTimeField(default=timezone.now)
    requester = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.headline


class Update(models.Model):
    notification = models.ForeignKey(Notification)
    update_number = models.PositiveIntegerField(default=1)
    updated_at = models.DateTimeField(default=timezone.now)
    next_update_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(default="Put the update content here.")

    def __unicode__(self):
        return str(self.update_number)
