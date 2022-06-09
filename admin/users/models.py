from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class Permission(models.Model):
#     name = models.CharField(max_length=200)


# class Role(models.Model):
#     name = models.CharField(max_length=200)
#     permissions = models.ManyToManyField(Permission)


class User(AbstractUser):
    first_name  = models.CharField(max_length=200)
    last_name   = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

    # role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    '''     AbstractUser has default username field
        we dont want to use username field but use email as username instead
    '''
    username = None
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []