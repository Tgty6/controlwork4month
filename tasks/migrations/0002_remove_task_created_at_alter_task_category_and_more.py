# Generated by Django 5.1.6 on 2025-02-27 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.category'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(),
        ),
    ]
