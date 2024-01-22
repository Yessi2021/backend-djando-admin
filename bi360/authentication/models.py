from typing import List

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        # Convert email to lowercase
        email = email.lower()

        # Create a regular user
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Convert email to lowercase
        email = email.lower()

        # Create a superuser
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    # Remueve el campo 'username'
    username = None

    email = models.EmailField(unique=True, verbose_name="Correo electrónico")

    # Sobrescribe la propiedad USERNAME_FIELD
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []

    objects = CustomUserManager()

    ordering = ["-date_joined"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
