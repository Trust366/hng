# Generated by Django 4.2.5 on 2023-09-07 20:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='utc_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
