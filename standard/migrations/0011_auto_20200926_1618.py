# Generated by Django 3.1.1 on 2020-09-26 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0010_remove_standard_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='chapter',
        ),
        migrations.AddField(
            model_name='subject',
            name='standard',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='standard.standard'),
            preserve_default=False,
        ),
    ]
