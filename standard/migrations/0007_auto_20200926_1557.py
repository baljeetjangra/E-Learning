# Generated by Django 3.1.1 on 2020-09-26 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0006_auto_20200926_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='chapter',
        ),
        migrations.AddField(
            model_name='chapter',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='standard.subject'),
            preserve_default=False,
        ),
    ]
