from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class staff(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    level = models.CharField(max_length=30)
    department = models.CharField(max_length=30, default="staff")
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    bloodGrp = models.CharField(max_length=3)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    img = models.ImageField(upload_to="data/images", default="empty")

    def __str__(self) -> str:
        return self.email.username