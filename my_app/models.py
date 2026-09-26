from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    USER_TYPES = [
        ('Admin','Admin'),
        ('Student','Student'),
        ('Teacher','Teacher'),
    ]
    
    user_type = models.CharField(
        max_length=20,null=True,
        choices=USER_TYPES
    )
    
    def __str__(self):
        return self.username

# common model 
class BasicInfoModel(models.Model):
    name = models.CharField(max_length=200,null=True)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=20,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    class Meta :
        abstract = True
    
class StudentModel(BasicInfoModel):
    user = models.OneToOneField(
        UserModel,on_delete=models.CASCADE,related_name='student_profile',
        null=True
    )
    roll_no = models.CharField(max_length=20,null=True)
    image = models.ImageField(upload_to='media/student_image',null=True)
    
    def __str__(self):
        return self.user.username
    
    
class TeacherModel(BasicInfoModel):
    user = models.OneToOneField(
            UserModel,on_delete=models.CASCADE,related_name='teacher_profile',
            null=True
        )
    image = models.ImageField(upload_to='media/teacher_image',null=True)
    
    def __str__(self):
        return self.user.username
    
