# Generated by Django 4.2 on 2023-05-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scavenger', '0002_remove_location_fun_fact'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_fun_fact',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True),
        ),
    ]
