from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

CATEGORY = (('ជីវភាព','ជីវភាព'),('សាលា','សាលា'),('ផ្សេងៗ','ផ្សេងៗ'))

class TodoModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    tododate = models.DateField(auto_now_add = True)
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY,
    )

    def __str__(self):
        return self.title

class AssignmentModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    deadline = models.DateTimeField()

    class Meta:
        ordering = ['-deadline']

    def __str__(self):
        return self.title
  
    def is_end_date(self):
        return timezone.now() > self.deadline

class NewsModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title