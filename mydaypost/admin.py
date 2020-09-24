from django.contrib import admin
from .models import TodoModel, AssignmentModel

# Register your models here.

admin.site.register(TodoModel)
admin.site.register(AssignmentModel)