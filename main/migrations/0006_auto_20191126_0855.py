# Generated by Django 2.2.7 on 2019-11-26 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_statement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='doctor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Doctor'),
        ),
    ]
