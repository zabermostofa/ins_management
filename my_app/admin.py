from django.contrib import admin
from .models import UserModel,TeacherModel,StudentModel
# Register your models here.

admin.site.register(
    [UserModel,TeacherModel,StudentModel]
)