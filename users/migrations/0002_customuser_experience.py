# Generated by Django 3.0.2 on 2020-04-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='experience',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
