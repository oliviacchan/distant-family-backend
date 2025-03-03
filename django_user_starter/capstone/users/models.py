from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True, help_text="User biography")
    birth_date = models.DateField(blank=True, null=True, help_text="Date of birth")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Phone number")
    address = models.TextField(blank=True, null=True, help_text="Contact address")
    role = models.CharField(max_length=50, blank=True, null=True, help_text="User role (e.g., admin, editor, etc.)")

    def __str__(self):
        return self.username
