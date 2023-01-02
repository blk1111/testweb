from django.db import models

# Create your models here.
class sp(models.Model):
    id = models.ForeignKey
    name = models.CharField(max_length=100)
    png = models.CharField(max_length=200)
    price = models.CharField(max_length=20)   
    class Meta:
        db_table = 'sp'
        
class ssp(models.Model):
    id = models.ForeignKey
    sname = models.CharField(max_length=100)
    spng = models.CharField(max_length=200)
    spic = models.CharField(max_length=20)
    class Meta:
        db_table = 'ssp'