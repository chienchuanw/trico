# Generated by Django 5.1.4 on 2024-12-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
