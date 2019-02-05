from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class ECC(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    pan_id = models.IntegerField(unique=True)
    gender =  models.CharField(max_length=15)
    password =  models.CharField(max_length=264)
    phone_number = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    employee_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.first_name
