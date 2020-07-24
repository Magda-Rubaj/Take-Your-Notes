from django.db import models
from ..user.models import User


class Category(models.Model):
    name = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    
    

    