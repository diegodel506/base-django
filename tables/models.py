from django.db import models

# Create your models here.
""" class Table(models.Model):
    number = models.IntegerField(unique=True)
    area = models.ForeignKey('areas.Area', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"Number: {self.number}      Area: {self.area}" """
        
class Table(models.Model):
    number = models.IntegerField()
    area = models.ForeignKey('areas.Area', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Mesa {self.number} Area {self.area}"

