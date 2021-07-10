# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.utils.timezone import now 

# Create your models here.
#class Imagess(models.Model)  
class BlogComment(models.Model):
    sno = models.AutoField(primary_key =True)
    comment= models.TextField()
    post = models.TextField() 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)
