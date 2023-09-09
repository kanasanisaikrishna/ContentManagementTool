
from django.db import models
from django.contrib.auth.models import User

class Blogs(models.Model):

    title=models.CharField(max_length=1200,null=True)
    Image=models.ImageField(null=True,blank=True)
    description=models.CharField(max_length=1200,null=True)
    date=models.DateField(auto_now_add=True,null=True)
    likes=models.IntegerField(default=0)
    
    auther =  models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def str(self):
        return self.title