# Generated by Django 3.1.1 on 2020-09-24 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0008_auto_20200924_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='file',
            new_name='upload_file',
        ),
    ]