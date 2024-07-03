from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    


        

