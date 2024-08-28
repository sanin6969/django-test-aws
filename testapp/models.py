from django.db import models

# Create your models here.
class Users(models.Model):
    Username= models.CharField( max_length=50,unique=True)
    Password= models.CharField( max_length=50) 
    Confirm_password= models.CharField(max_length=50)   
    def __str__(self) -> str:
        return self.Username
    
class User_profile(models.Model):
    f_username=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='User_profile')
    my_username=models.CharField(max_length=50)
    my_password=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.my_username
    
class destination(models.Model):
    d_username=models.CharField( max_length=50)
    d_password=models.CharField( max_length=50)
    d_foreignkey=models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.d_username