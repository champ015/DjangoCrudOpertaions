from django.db import models
class Position(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title
        
class employee(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    empcode=models.CharField(max_length=200)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    

