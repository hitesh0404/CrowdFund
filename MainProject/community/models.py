from django.db import models

"""
Tables  

Project/motive        

over one motive there can be multiple group     one motive--> many group

Group                          will contain one foreign key from Motive


InitiatorGroupContributor 


groupContributor               
                               will contain one foreign key from Contributor
                               will contain one foreign key from Motive 
                               role 
                               inatiator          7738526577       devashi raghunath
"""
class MotiveType(models.TextChoices):
    SOCIAL_CAUSE = 'Social Cause', 'Social Cause'
    ENVIRONMENTAL = 'Environmental', 'Environmental'
    EDUCATIONAL = 'Educational', 'Educational'
    MEDICAL = 'Medical', 'Medical'
    CHARITY = 'Charity', 'Charity'
    OTHER = 'Other', 'Other'

class Motive(models.Model):
    name=models.CharField(max_length=40,unique=True)
    logo=models.ImageField()
    motive_type = models.CharField(
        max_length=50,
        choices=MotiveType.choices,
        default=MotiveType.SOCIAL_CAUSE,
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)