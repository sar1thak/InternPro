from django.db import models
from django.contrib.auth.models import User

class Internship(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Applied')
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.role}"


class Task(models.Model):
    completed = models.BooleanField(default=False)
    PRIORITY = [
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    deadline = models.DateField()
    priority = models.CharField(max_length=20, choices=PRIORITY)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
