import uuid

from django.db import models


class UserModel(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobileNumber = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, unique=True)
    password = models.BinaryField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
