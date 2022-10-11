from unittest.util import _MAX_LENGTH
from django.db import models

class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    author = models.TextField()
    url = models.TextField()
    views = models.IntegerField()

    class Meta:
        ordering = ['created']

class Comment(models.Model) :
    created = models.DateTimeField(auto_now_add=True)
    username = models.TextField()
    commentText = models.TextField()
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='comments')

    class Meta:
        ordering = ['created']