from django.db import models
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'Course "{self.name}"'

    @property
    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date


class Lecture(models.Model):
    lecture_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    week = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    url = models.TextField()

    def __str__(self):
        return f'"{self.name}"'


class Task(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    due_date = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Task "{self.name}"'


class Solution(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)
    url = models.TextField()

    def __str__(self):
        return f'Solution to Task {self.task}'
