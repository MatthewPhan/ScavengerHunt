# Generated by Django 4.2 on 2023-04-16 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scavenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='location_name',
        ),
        migrations.RemoveField(
            model_name='location',
            name='code',
        ),
        migrations.AddField(
            model_name='location',
            name='qrcode_filepath',
            field=models.ImageField(blank=True, upload_to='qrcodes'),
        ),
    ]
