# coding: utf-8
from django.db import models
from educommon.django.db.models import BaseModel


class Test(BaseModel):

    candidate = models.ForeignKey(
        'Candidate.Candidate',
        verbose_name=u'Candidate',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = u'Test'
        verbose_name_plural = u'Tests'

    def __unicode__(self):
        return (u'%s' % str(self.name)).encode('utf-8')

    def __str__(self):
        return (u'%s' % str(self.name)).encode('utf-8')
