# Generated by Django 3.1.1 on 2020-09-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0015_auto_20200926_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.CharField(default='math', max_length=50),
            preserve_default=False,
        ),
    ]
