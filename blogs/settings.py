# -*- coding: utf-8 -*-
from django.conf import settings

CREATED = 'ADD'
PUBLISHED = 'PUB'
CANCELED = 'CAN'
BANNED = 'BAN'

DEFAULT_STATS = (
    (CREATED, 'Created'),
    (PUBLISHED, 'Published'),
    (CANCELED, 'Canceled'),
    (BANNED, 'Banned')
)

STATS = getattr(settings, 'STATS', DEFAULT_STATS)