from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from harnas.checker.models import TestEnvironment


class Contest(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User)

    class Meta:
        permissions = (
            ('view', 'Can view'),
            ('participate', 'Can participate'),
            ('manage', 'Can manage contest'))

    def __str__(self):
        return self.name


class ContestForm(ModelForm):

    class Meta:
        model = Contest
        fields = ['name', 'description']


class News(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    contest = models.ForeignKey(Contest)

    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return self.title


class NewsForm(ModelForm):
    
    class Meta:
        model = News
        fields = ['title', 'description']


class Task(models.Model):
    name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=3)
    description = models.TextField()
    test_environment = models.ForeignKey(TestEnvironment)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.name


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'short_name', 'description', 'test_environment']


class TestCase(models.Model):
    task = models.ForeignKey(Task)
    max_memory = models.PositiveIntegerField()
    max_duration = models.PositiveIntegerField()
