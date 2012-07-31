from django.db import models

class Token(models.Model):
    created = models.DateTimeField("Creation date/time", auto_now_add=True)
    token = models.CharField("Facebook access token", max_length=80)
    user_id = models.CharField("Facebook user id", max_length=16)
    expires = models.DateTimeField("Date/time of token expiry")

    def __str__(self):
        return "%s %s %s" % (self.expires, self.user_id, self.token)
