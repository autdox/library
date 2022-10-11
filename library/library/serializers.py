from unittest.util import _MAX_LENGTH
from pkg_resources import require
from rest_framework import serializers
from library.library.models import Book
from library.library.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = [
            'pk',
            'created',
            'username',
            'commentText',
            'bookId',
        ]

class BookSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Book
        fields = [
            'pk', 
            'title', 
            'author', 
            'url', 
            'views',
            
            'comments',
            ]