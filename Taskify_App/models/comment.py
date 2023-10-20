from django.db import models
from ckeditor.fields import RichTextField
from .card import Card
from .user import User

class Comment(models.Model):
    text=RichTextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    card=models.ForeignKey(Card,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return f'{self.author}({self.message})'
#done