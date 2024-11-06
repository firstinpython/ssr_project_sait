from django.db import models

# Create your models here.


class ProjectsModel(models.Model):
    name_project = models.CharField(verbose_name="name_project",max_length=120)
    description_project = models.TextField(verbose_name="description_project",max_length=10000)
    date_of_creation = models.DateField(verbose_name="date_of_creation",auto_now=True)
    date_of_update = models.DateField(verbose_name="date_update",auto_now_add=True)
    status = models.ForeignKey(verbose_name="StatusModel",to="StatusModel",on_delete=models.CASCADE,null=True)


class StatusModel(models.Model):
    name_status = models.CharField(verbose_name="name_status",max_length=120)