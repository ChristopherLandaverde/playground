from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Inversion(models.Model):
    idea = models.CharField(max_length=255,blank=False,null=False)
    reversed_idea=  models.CharField(max_length=255,blank=False,null=False)
    wrong= models.CharField(max_length=255,blank=False,null=False)
    created_by = models.ForeignKey(User,related_name='invertthoughts',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return '%s' % self.idea

        