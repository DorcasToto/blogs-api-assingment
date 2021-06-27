from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.utils.translation import ugettext as _

# Create your models here.

class User(AbstractUser):

    username = CharField(null=True,max_length=255, unique=True)
    email = CharField(blank=True, null=True,max_length=255)

    def __str__(self):
        return self.username

class Blog(models.Model):
    blogTitle= CharField( null=True,max_length=255, unique=False)
    blogDescription= CharField( null=True,max_length=255, unique=False)
    user=models.ForeignKey(User, related_name='name', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.blogTitle
