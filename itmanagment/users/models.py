

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


# Create your models here.

class UsersModel(AbstractUser):
    age = models.IntegerField(verbose_name="age", validators=[MinValueValidator(0)],null=True)
    role = models.ForeignKey(to="RoleModel", on_delete=models.CASCADE,null=True)
    profession_category = models.ForeignKey(to="ProfessionCategoryModel", on_delete=models.CASCADE,null=True)
    dev_stack = models.ManyToManyField(to='DevStackModel', null=True)
    avatar = models.FileField(upload_to="avatar_user", null=True)
    create_projects = models.BooleanField(default=True)

    def create_project(self):
        if self.role.name_role == "РП":
            self.create_projects = True
        else:
            self.create_projects = False

    # def __str__(self):
    #     return f"{self.username}{self.create_projects}{self.pk}"


class DevStackModel(models.Model):
    user_stack = models.CharField(verbose_name="user_stack", max_length=120)

    def __str__(self):
        return f"Стэк {self.user_stack}"


class ProfessionCategoryModel(models.Model):
    name_prof_category = models.CharField(verbose_name="name_prof_category", max_length=120)

    def __str__(self):
        return f"{self.name_prof_category}"


class RoleModel(models.Model):
    """ Роль на проекте и для пользователя"""
    name_role = models.CharField(verbose_name="name_role", max_length=120)

    def __str__(self):
        return f"{self.name_role}"


class WebSocketsModel(models.Model):
    name = models.CharField(max_length=120)
    user = models.ManyToManyField(to=UsersModel, verbose_name="user")
