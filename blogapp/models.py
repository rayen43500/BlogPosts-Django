from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
