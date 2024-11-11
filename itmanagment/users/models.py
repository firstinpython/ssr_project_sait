from distutils.command.upload import upload

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from projects.models import ProjectsModel
# Create your models here.

class UsersModel(AbstractUser):
    age = models.IntegerField(verbose_name="age", validators=[MinValueValidator(0)])
    role = models.ForeignKey(to="RoleModel", on_delete=models.CASCADE)
    profession_category = models.ForeignKey(to="ProfessionCategoryModel",on_delete=models.CASCADE)
    dev_stack = models.ForeignKey(to='DevStackModel',on_delete=models.CASCADE,null=True)
    avatar = models.FileField(upload_to="avatar_user",null=True)
    projects = models.ManyToManyField(to=ProjectsModel,null=True)
    create_projects = models.BooleanField(default=True)



class DevStackModel(models.Model):
    user_stack = models.CharField(verbose_name="user_stack",max_length=120)


class ProfessionCategoryModel(models.Model):
    name_prof_category = models.CharField(verbose_name="name_prof_category",max_length=120)


class RoleModel(models.Model):
    name_role = models.CharField(verbose_name="name_role", max_length=120)

    def __str__(self):
        return f"{self.name_role}"
