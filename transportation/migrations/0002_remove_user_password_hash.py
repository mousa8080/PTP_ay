# Generated by Django 5.1.6 on 2025-03-14 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password_hash',
        ),
    ]
