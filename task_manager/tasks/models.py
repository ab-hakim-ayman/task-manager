from django.db import models
from django.contrib.auth.models import User

# Create a custom priority choices tuple
PRIORITY_CHOICES = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    photos = models.ImageField(upload_to='images')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    is_complete = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='task_photos/')

    def __str__(self):
        return f'Photo for Task: {self.task.title}'
