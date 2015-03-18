from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __unicode__(self):
        return self.firstname

    @models.permalink
    def get_absolute_url(self):
        return ('user-detail', [self.id])