from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

CATEGORY = (('ជីវភាព','ជីវភាព'),('សាលា','សាលា'),('ផ្សេងៗ','ផ្សេងៗ'))
STATE = (('សកម្ម','សកម្ម'),('រួចរាល់','រួចរាល់'),('ខកខាន','ខកខាន'))

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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    deadline = models.DateTimeField()
    state = models.CharField(
        max_length = 50,
        choices = STATE,
    )
    class Meta:
        ordering = ['-state']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.deadline < timezone.now():
            self.state = STATE[2][0]
        super(AssignmentModel, self).save(*args, **kwargs)





