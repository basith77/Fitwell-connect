from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=50)
    bf = models.IntegerField()
    lu = models.IntegerField()
    di = models.IntegerField()
    cal = models.IntegerField()
    fat = models.IntegerField()
    pro = models.IntegerField()
    sug = models.IntegerField()
    imagepath= models.CharField(default="",max_length=100)

    def __str__(self):
        return self.name

class Yoga(models.Model):
    yoga_name = models.CharField(max_length=100)
    image = models.FileField('Upload Image',upload_to='')
    description = models.TextField(max_length=2000)
    min_val_bmi = models.CharField(max_length=100)
    max_val_bmi = models.CharField(max_length=100)
    youtube_link = models.CharField(max_length=300)
    def __str__(self):
        return self.yoga_name