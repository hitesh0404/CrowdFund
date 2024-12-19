from django.db import models

from accounts.models import Contributor
from uuid import uuid4
"""
Tables  

Project/motive        

over one motive there can be multiple group     one motive--> many group

Group                          will contain one foreign key from Motive


InitiatorGroupContributor 


groupContributor               
                               will contain one foreign key from Contributor
                               will contain one foreign key from Group 
                               role 
                               inatiator          
"""
class MotiveType(models.TextChoices):
    SOCIAL_CAUSE = 'Social Cause', 'Social Cause'
    ENVIRONMENTAL = 'Environmental', 'Environmental'
    EDUCATIONAL = 'Educational', 'Educational'
    MEDICAL = 'Medical', 'Medical'
    CHARITY = 'Charity', 'Charity'
    OTHER = 'Other', 'Other'

class Motive(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,auto_created=True)
    name=models.CharField(max_length=40,unique=True)
    # contributor = models.ManyToManyField(Contributor,through='InitiatorGroupContributor')
    logo=models.ImageField(upload_to="image/motive/logo/")
    motive_type = models.CharField(
        max_length=50,
        choices=MotiveType.choices,
        default=MotiveType.SOCIAL_CAUSE,
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class RoleType(models.TextChoices):
    ADMIN = 'Admin','Admin'
    CREATOR = 'Creator','Creator'
    USER = 'User','User'

class Group(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,auto_created=True)
    created_by = models.ForeignKey(Contributor,on_delete=models.DO_NOTHING)
    dp = models.ImageField(upload_to="image/group/dp/")
    name = models.CharField(max_length=50,null=False,blank=False,default=id)
    motive = models.ForeignKey(Motive,on_delete=models.DO_NOTHING)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
class InitiatorGroupContributor(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,auto_created=True)
    contributor = models.ForeignKey(Contributor,on_delete=models.DO_NOTHING)
    # motive = models.ForeignKey(Motive,on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group,on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    role = models.CharField( max_length=50,
        choices=RoleType.choices,
        default=RoleType.USER,
        )
    class Meta:
        unique_together = ['contributor','group']

class GroupContributor(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,auto_created=True)
    contributor = models.ForeignKey(Contributor,on_delete=models.DO_NOTHING)
    # motive = models.ForeignKey(Motive,on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group,on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    role = models.CharField( max_length=50,
        choices=RoleType.choices,
        default=RoleType.USER,
        )
    class Meta:
        unique_together = ['contributor','group']