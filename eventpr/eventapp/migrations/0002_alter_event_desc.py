# Generated by Django 5.0.4 on 2024-05-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.CharField(max_length=100),
        ),
    ]
