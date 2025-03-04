from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    credit = models.IntegerField()
    
    def __str__(self):
        return f"{self.code} - {self.name}"