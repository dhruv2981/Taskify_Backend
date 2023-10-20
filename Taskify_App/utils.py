import secrets
from Taskify_App.models import *

def generate_unique_colour():
    while True:
        color='#'+secrets.token_hex(3)
        if not List.objects.filter(color=color).exists():
            return color