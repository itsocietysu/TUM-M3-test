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


class Question(BaseModel):
    text = models.TextField(max_length=1000)

    class Meta:
        verbose_name = u'Question'
        verbose_name_plural = u'Questions'

    def __unicode__(self):
        return (u'%s' % str(self.name)).encode('utf-8')

    def __str__(self):
        return (u'%s' % str(self.name)).encode('utf-8')


class TestResult(models.Model):
    
    test = models.ForeignKey(
        Test, 
        verbose_name=u'Test', 
        on_delete=models.CASCADE
    )
    
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE
    )
    answer = models.BooleanField()
    
    class Meta:
        verbose_name = u'TestResult'
        verbose_name_plural = u'TestResults'

    def __unicode__(self):
        return (u'%s' % str(self.name)).encode('utf-8')

    def __str__(self):
        return (u'%s' % str(self.name)).encode('utf-8')
