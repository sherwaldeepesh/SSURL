from django.db import models
from.utils import code_generator, create_shortcode
from django.conf import settings
from .validators import validate_dot_com,validate_url
from django.urls import reverse
from django_hosts.resolvers import reverse

# Create your models here.

shorturl_max = getattr(settings, "shorturl_max", 10)

class ssurlURLmanager(models.Manager):
    def all(self, *args, ** kwargs):
        qs_main = super(ssurlURLmanager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs
    
    def refresh_shorturl(self, items=100):
        qs = ssurlURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[::items]
        nw=0
        for q in qs:
            q.shorturl = create_shortcode(q)
            print(q.id)
            q.save()
            nw += 1
        return "New codes made: {i}".format(i=nw)


class ssurlURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url])
    shorturl = models.CharField(max_length=shorturl_max ,unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  #Everytie the model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when the model was created
    active = models.BooleanField(default=True)
    # empty_datetime = models.DateTimeField(auto_now=True,auto_now_add=True)
    # shorturl = models.CharField(max_length=10,null=False, blank=False)
    # shorturl = models.CharField(max_length=10,null=True)  empty in db is okay
    # shorturl = models.CharField(max_length=10,default='shortcode')

    objects = ssurlURLmanager()
    # some_random = ssurlURLmanager()

    def save(self,*args,**kwargs):
        if self.shorturl is None or self.shorturl == "":
            self.shorturl = create_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(ssurlURL, self).save(*args, ** kwargs)

    # class Meta:
    #     ordering = '-id'

    

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        # print(self.shorturl)
        url_path = reverse("shorturlURL", kwargs={"shorturl":self.shorturl},host='www',scheme='http')
        return url_path