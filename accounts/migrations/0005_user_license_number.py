# Generated by Django 5.1.6 on 2025-03-04 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_license_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='license_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
