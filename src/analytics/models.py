from django.db import models
from shortner.models import ssurlURL

# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance,ssurlURL):
            obj, created = self.get_or_create(ssurl_URL=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    ssurl_URL = models.OneToOneField(ssurlURL,on_delete=models.PROTECT)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)  
    timestamp = models.DateTimeField(auto_now_add=True) 

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)