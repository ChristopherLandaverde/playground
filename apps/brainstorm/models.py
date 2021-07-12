from django.contrib.auth.models import User 
from django.db import models


# Create your models here.

class Brainstorm(models.Model):
    goals = models.CharField(max_length=255,blank=True,null=True)
    agenda= models.CharField(max_length=255,blank=True,null=True)
    outcomes= models.CharField(max_length=255,blank=True,null=True)
    decisions= models.CharField(max_length=255,blank=True,null=True)
    created_by = models.ForeignKey(User,related_name='brainstorms',on_delete=models.CASCADE,null=True)


    def __str__(self):
        return '%s' % self.goals