from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TODO(models.Model):
  srno = models.AutoField(primary_key=True,auto_created=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=80)
  date = models.DateTimeField(auto_now_add=True)
  