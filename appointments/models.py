from django.db import models
from patients.models import patients
from staff.models import staff
from django.contrib.auth.models import User
# Create your models here.
class appointment(models.Model):
    pat = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_name")
    doc = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_name")
    department = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()