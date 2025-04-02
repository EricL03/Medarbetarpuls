from __future__ import annotations
from django.db import models
from django.db.models.manager import BaseManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import logging
from typing import cast


# Create your models here.


class EmailList(models.Model):
    email = models.EmailField(unique=True)
    
