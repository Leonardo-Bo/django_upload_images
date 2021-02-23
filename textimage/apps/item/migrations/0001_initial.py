# Generated by Django 3.1.7 on 2021-02-23 09:27

import apps.item.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.item.models.image_upload_to)),
                ('reftext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.textmodel')),
            ],
        ),
    ]