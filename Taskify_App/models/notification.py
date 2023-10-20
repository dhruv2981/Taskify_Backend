from django.db import models
from .user import User

class Notification(models.Model):
    id = models.AutoField( primary_key=True)
    text=models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField()
    redirection_link=models.URLField(blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notifications')

    def __str__(self):
        return f'self.text(self.user)'
#query parameter
