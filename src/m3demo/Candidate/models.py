# coding: utf-8
from django.db import models
from educommon.django.db.models import BaseModel


class Candidate(BaseModel):

    name = models.CharField(
        u'Name',
        max_length=200,
    )

    planet = models.ForeignKey(
        'Planet.Planet',
        verbose_name=u'Planet',
        null=True,
        on_delete=models.SET_NULL,
    )

    age = models.IntegerField(
        u'Age',
    )

    email = models.EmailField(
        u'Email',
        default='',
        max_length=100)

    jedi = models.ForeignKey(
        'Jedi.Jedi',
        verbose_name=u'Jedi',
        default=None,
        null=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name = u'Candidate'
        verbose_name_plural = u'Candidates'

    def __unicode__(self):
        return (u'%s' % str(self.name)).encode('utf-8')

    def __str__(self):
        return (u'%s' % str(self.name)).encode('utf-8')
