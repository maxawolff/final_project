"""Models for WSCA Website."""


from django.db import models
from multiselectfield import MultiSelectField


class Meeting(models.Model):
    """Meeting model for CA site."""

    district = models.IntegerField()
    meeting_name = models.CharField(max_length=50)
    weekday_choices = [
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday'),
    ]
    weekday = models.CharField(max_length=10, choices=weekday_choices)
    start_time = models.CharField(max_length=15)
    end_time = models.CharField(max_length=15)
    location_name = models.CharField(max_length=150)
    street = models.CharField(max_length=250)
    suite = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zip_code = models.IntegerField()
    room = models.CharField(max_length=100)
    notes = models.TextField()
    duration = models.CharField(max_length=200)
    meeting_format_choices = [
        ('BB', 'Big Book Study'),
        ('C', 'Closed meeting for those with a desire to stop using cocaine and all other substances. Newcomers welcome.'),
        ('CL', 'Candlelight'),
        ('LS', 'Literature Study'),
        ('M', 'Men only'),
        ('NC', 'No children please.'),
        ('SB', 'Meeting has a smoke break.'),
        ('W', 'Women only.'),
        ('HC', 'Wheelchair accessible'),
    ]
    meeting_format = MultiSelectField(
        max_length=200,
        choices=meeting_format_choices,
    )
    accessibility = models.CharField(max_length=150)
    last_updated = models.DateTimeField(auto_now_add=True, null=True)


class ServiceMeeting(models.Model):
    """Service Meeting model for CA site."""

    meeting_name = models.CharField(max_length=100)
    meeting_day = models.CharField(max_length=100)
    start_time = models.CharField(max_length=15)
    location_name = models.CharField(max_length=150)
    street = models.CharField(max_length=250)
    suite = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zip_code = models.IntegerField()
    room = models.CharField(max_length=100)
    notes = models.TextField()
    last_updated = models.DateTimeField(auto_now_add=True, null=True)


class Events(models.Model):
    """Event model for CA site."""

    event_photo = models.ImageField(upload_to='')
    event_name = models.CharField(max_length=50)
    weekday_choices = [
        ('sun', 'Sunday'),
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
    ]
    start_time = models.CharField(max_length=15)
    end_time = models.CharField(max_length=15)
    location_name = models.CharField(max_length=150)
    street = models.CharField(max_length=250)
    suite = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zip_code = models.IntegerField(null=True)
    room = models.CharField(max_length=100)
    notes = models.TextField()
    accessibility = models.CharField(max_length=150)
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
    event_date = models.DateTimeField(null=True)
    published = models.BooleanField(default=False)
    contact_phone = models.CharField(max_length=15, null=True)


class InternalResources(models.Model):
    """Resource model for CA site."""

    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500, blank=True, default='')
    upload = models.FileField(upload_to='')
