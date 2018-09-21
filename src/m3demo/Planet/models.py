# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from educommon.django.db.models import BaseModel

class Planet(BaseModel):

    name = models.CharField(
        u'Name',
        max_length=100,
    )

    class Meta:
        verbose_name = u'Planet'
        verbose_name_plural = u'Planets'


    def __unicode__(self):
        return (u'%s' % str(self.name)).encode('utf-8')

    def __str__(self):
        return (u'%s' % str(self.name)).encode('utf-8')
