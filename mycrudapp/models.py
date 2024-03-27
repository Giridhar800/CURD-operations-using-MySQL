from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=20)
    umail = models.EmailField(max_length=200)
    upassword = models.CharField(max_length=30)

    class Meta:
        db_table = 'users'

