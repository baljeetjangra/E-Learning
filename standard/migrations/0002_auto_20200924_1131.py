# Generated by Django 3.1.1 on 2020-09-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='standard',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]