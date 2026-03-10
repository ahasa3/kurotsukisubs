from django.db import models
from django.utils.text import slugify

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=255, blank=True, null=True)

    @property
    def post_count(self):
        return self.posts.count()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class DownloadLink(models.Model):
    HOST_CHOICES = [
        ('gdrive', 'Google Drive'),
        ('trakteer', 'Trakteer'),
        ('other', 'Other'),
    ]
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='downloads')
    label = models.CharField(max_length=100)
    url = models.URLField()
    host = models.CharField(max_length=20, choices=HOST_CHOICES, default='other')
    file_size = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.label


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=True)
    content = models.TextField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    category = models.CharField(max_length=50, default='General')
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title