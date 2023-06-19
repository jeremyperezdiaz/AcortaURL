from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000,  verbose_name="Link")
    uuid = models.CharField(max_length=10,  verbose_name="Unique ID")
    
    def __str__(self):
        return "ID: {} - URL: {}".format(self.uuid, self.link)