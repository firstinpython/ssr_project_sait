from django.db import models
from projects.models import ProjectsModel
from users.models import UsersModel
# Create your models here.

class TaskModel(models.Model):
    name_task = models.CharField(verbose_name="name_task",max_length = 120)
    description_task = models.TextField(verbose_name = "description_task")
    project = models.ForeignKey(to=ProjectsModel,on_delete=models.CASCADE)
    status = models.ForeignKey(to="StatusTaskModel",on_delete=models.CASCADE)
    executor = models.ForeignKey(to = UsersModel,on_delete=models.CASCADE,related_name="executor_task")
    priority = models.ForeignKey(to="PriorityTaskModel",on_delete=models.CASCADE)
    date_of_creation = models.DateField(verbose_name="date_of_creation",auto_now=True)
    date_of_update = models.DateField(verbose_name="date_of_update",auto_now_add=True)
    date_of_deadline = models.DateField(verbose_name='date_of_deadline',null=True)
    resp_for_testing = models.ForeignKey(to=UsersModel,on_delete=models.CASCADE,related_name="resp_task")


    def __str__(self):
        return f"{self.name_task} | {self.executor}"


class StatusTaskModel(models.Model):
    name_status = models.CharField(verbose_name="name_status",max_length=120)

    def __str__(self):
        return f"{self.name_status}"

class PriorityTaskModel(models.Model):
    name_priority = models.CharField(verbose_name="name_priority",max_length=120)

    def __str__(self):
        return f"{self.name_priority}"


class Comments(models.Model):
    username = models.ForeignKey(verbose_name="username", to=UsersModel, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="description")
    datetime = models.DateTimeField(verbose_name='data',auto_now_add=True)

    def __str__(self):
        return f"{self.username} | {self.datetime}"