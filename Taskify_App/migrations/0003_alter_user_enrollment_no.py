# Generated by Django 4.1.12 on 2023-11-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskify_App', '0002_alter_user_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='enrollment_no',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
