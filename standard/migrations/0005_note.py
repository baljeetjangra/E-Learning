# Generated by Django 3.1.1 on 2020-09-26 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0004_remove_chapter_chapter_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('upload_file', models.FileField(upload_to='notes/%Y/%m/%d/')),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chapter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='standard.chapter')),
            ],
        ),
    ]
