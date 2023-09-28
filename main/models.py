from django.db import models

# Create your models here.

class Motors(models.Model):
    name=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    mileage=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)


    def __str__(self):
        return self.name