# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.

class User(models.Model):
	userid = models.AutoField(primary_key=True)
	username = models.CharField(max_length=200)
	
	def __unicode__(self):
		return unicode(self.username)
	
	class Meta:
		db_table = u'UserDetails'


class Task(models.Model):
	taskid = models.AutoField(primary_key=True)
	userid = models.ForeignKey(User,db_column='userid')
	taskname = models.CharField(max_length=200)
	starttime = models.DateTimeField(default=datetime.now, blank=True)
	endtime = models.DateTimeField(default=datetime.now, blank=True)
	duration = models.IntegerField(default=0)
	status = models.CharField(max_length=200,default='start')
	def __unicode__(self):
		return unicode(self.taskname)
	
	class Meta:
		db_table = u'TaskDetails'	
