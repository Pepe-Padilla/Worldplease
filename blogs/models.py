from django.db import models
from django.contrib.auth.models import User
from blogs.settings import STATS

class Blog(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    resumen = models.CharField(max_length=500)
    cuerpo = models.TextField(blank=True, null=True, default="")
    urlImg = models.URLField(blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATS)

    def __unicode__(self): #metodo de 0 parametros
        return self.title
