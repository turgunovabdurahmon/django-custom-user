from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    
    telefon_raqam = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(default=2)
    avatar = models.ImageField(upload_to="user-avatar/", blank=True, null=True)

    REQUIRED_FIELDS = ["age", "telefon_raqam"]
    


    def __self__(self):
        return self.telefon_raqam

