from datetime import datetime

from django.db import models


class Threaddb(models.Model):
    threadname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastdate = models.DateField(default=datetime.now)

    def __str__(self):
        return str(self.threadname)

class threadcontentdb(models.Model):
    threadid = models.ForeignKey(Threaddb,on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now)
    content = models.TextField()

    def __str__(self):
        return str(self.contentid)

class thread_deleterequestdb(models.Model):
    delete_threadid = models.IntegerField()
    reason_delete = models.TextField()

    def __str__(self):
        return str(self.delete_threadid)

class threadcontent_deleterequestdb(models.Model):
    delete_contentid = models.IntegerField()
    reason_delete = models.TextField()

    def __str__(self):
        return str(self.delete_contentid)

class manager_userdb(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return str(self.username)

# Create your models here.
