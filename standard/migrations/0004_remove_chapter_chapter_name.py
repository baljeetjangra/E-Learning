# Generated by Django 3.1.1 on 2020-09-26 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0003_auto_20200926_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='chapter_name',
        ),
    ]
