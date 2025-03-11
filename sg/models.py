from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #  Each TODO belongs to a user
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)  # Check if the task is completed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
