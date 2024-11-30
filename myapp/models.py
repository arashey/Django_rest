from django.db import models

class productModels(models.Model):
    tittle=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
