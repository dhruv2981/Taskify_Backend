from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Log)
admin.site.register(Notification)
admin.site.register(Project)
admin.site.register(Card)
admin.site.register(List)
admin.site.register(Project_role)
