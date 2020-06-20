from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):

    
    user    =   models.OneToOneField(User,on_delete=models.CASCADE)

    # additional user attributes
    portfolio   =   models.URLField(blank=True)
    propic      =   models.ImageField(upload_to='propics',blank=True)

    def __str__(self):
        return self.user.username
