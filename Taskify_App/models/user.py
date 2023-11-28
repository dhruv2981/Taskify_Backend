from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    user_role = [
        ('a', 'admin'),
        ('n', 'normal_user')
    ]
    
    name = models.CharField(max_length=60)
    year = models.IntegerField(null=True,blank=True)
    enabled=models.BooleanField(default=True)
    role=models.CharField(max_length=1,choices=user_role,default='n')
    email=models.EmailField(max_length=60)
    enrollment_no=models.BigIntegerField(unique=True,null=True,blank=True)
    image=models.CharField(null=True,blank=True,max_length=400)

    # Provide unique related_name arguments to avoid clashes
    # groups = models.ManyToManyField(Group, related_name='custom_user_set')
    # user_permissions = models.ManyToManyField(
    #     Permission, related_name='custom_user_set')
    

    

    class Meta:
        unique_together=('name','enrollment_no')

    # def __str__(self):
    #     return self.username
#done(see video custom user model)