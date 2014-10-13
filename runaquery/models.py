from django.db import models

# Create your models here.
class QueryOptions(models.Model):
    biginteger = models.BigIntegerField()

    def __unicode__(self):
        return str(self.biginteger)

