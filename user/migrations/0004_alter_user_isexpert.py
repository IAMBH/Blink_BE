# Generated by Django 5.0 on 2024-02-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isExpert',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
