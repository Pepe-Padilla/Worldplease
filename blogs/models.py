from django.db import models

CREATED = 'ADD'
PUBLISHED = 'PUB'
CANCELED = 'CAN'
BANNED = 'BAN'

STATS = (
    (CREATED, 'Created'),
    (PUBLISHED, 'Published'),
    (CANCELED, 'Canceled'),
    (BANNED , 'Banned')
)


class Blog(models.Model):
    title = models.CharField(max_length=150)
    resumen = models.CharField(max_length=500)
    cuerpo = models.TextField(blank=True, null=True, default="")
    urlImg = models.URLField()
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATS)

    def __unicode__(self): #metodo de 0 parametros
        return self.title
