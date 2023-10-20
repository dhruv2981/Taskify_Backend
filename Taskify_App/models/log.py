from django.db import models
from .user import User

class Log(models.Model):
    # log_type=[
    #     (),
    # ]
    id = models.AutoField(primary_key=True)
    # type=models.CharField(choices=log_type)
    message=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'self.message(self.user)'

