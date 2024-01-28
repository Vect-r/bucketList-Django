from django.db import models
from datetime import datetime

# Create your models here.
class BucketList(models.Model):
	BLid = models.AutoField(primary_key=True)
	Name = models.TextField(unique=True,null=False,blank=False)
	isDone = models.BooleanField(default=False)
	DateCreated = models.DateField()
	DateModified = models.DateField()