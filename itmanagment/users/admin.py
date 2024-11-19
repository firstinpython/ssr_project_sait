from django.contrib import admin
from .models import UsersModel, DevStackModel, ProfessionCategoryModel, RoleModel,WebSocketsModel
# Register your models here.

admin.site.register(UsersModel)
admin.site.register(DevStackModel)
admin.site.register(ProfessionCategoryModel)
admin.site.register(RoleModel)
admin.site.register(WebSocketsModel)