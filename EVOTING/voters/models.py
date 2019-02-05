from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class Voters(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    voter_id = models.CharField(max_length=11, unique=True)
    pan_id = models.CharField(max_length=10, unique=True)
    gender =  models.CharField(max_length=15)
    Age = models.IntegerField(validators=[MaxValueValidator(110)])
    password =  models.CharField(max_length=264)
    location = models.CharField(max_length=264)
    phone_number = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    vote_flag = models.IntegerField(default=1)
    user_flag = models.IntegerField(default=0)
    def __str__(self):
        return self.first_name
