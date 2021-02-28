from django.db import models

# Create your models here.


class Qustions(models.Model):
    qestion_id = models.CharField(max_length=100)
    qestion_topic = models.CharField(max_length=100)
    qestion_no = models.CharField(max_length=100)
    qestion = models.CharField(max_length=100)  
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)