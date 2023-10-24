from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class patients(models.Model):
    fname = models.CharField(max_length= 20)
    lname = models.CharField(max_length= 20)
    state = models.CharField(max_length= 40)
    city = models.CharField(max_length= 50)
    pincode = models.CharField(max_length= 8)
    address = models.CharField(max_length= 100)
    phone = models.CharField(max_length=10)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    marr = models.CharField(max_length=10)
    empl = models.CharField(max_length=10)
    img = models.ImageField(upload_to="data/images")

    def __str__(self) -> str:
        return self.email.username