from django.contrib import admin
from .models import TodoModel, AssignmentModel, NewsModel, CommentModel

# Register your models here.

admin.site.register(TodoModel)
admin.site.register(AssignmentModel)
admin.site.register(NewsModel)
admin.site.register(CommentModel)