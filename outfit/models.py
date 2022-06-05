from django.db import models

# Create your models here.

class musinsa_model(models.Model):
    musinsa_key = models.IntegerField(primary_key = True)
    musinsa_image = models.TextField()
    musinsa_link = models.TextField()

    class Meta:
        db_table = 'musinsa'
