
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Cubing(models.Model):

    described_idea = models.CharField(max_length=255,blank=False,null=True)
    compared_idea = models.CharField(max_length=255,blank=False,null=True)
    associate_idea = models.CharField(max_length=255,blank=False,null=True)
    analyzed_idea = models.CharField(max_length=255,blank=False,null=True)
    applyed_idea = models.CharField(max_length=255,blank=False,null=True)
    argued_idea =models.CharField(max_length=255,blank=False,null=True)
    created_by = models.ForeignKey(User,related_name='cubing',on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.described_idea

        
