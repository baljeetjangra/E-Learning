# Generated by Django 3.1.1 on 2020-09-26 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0005_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='chapter',
        ),
        migrations.AddField(
            model_name='subject',
            name='chapter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='standard.chapter'),
            preserve_default=False,
        ),
    ]