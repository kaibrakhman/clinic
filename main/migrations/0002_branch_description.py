# Generated by Django 2.2.7 on 2019-11-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='description',
            field=models.TextField(default=''),
        ),
    ]