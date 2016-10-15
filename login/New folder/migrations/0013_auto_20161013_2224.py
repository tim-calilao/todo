# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 14:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0012_emailcheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcheck',
            name='activity',
            field=models.ForeignKey(default='default_activity', on_delete=django.db.models.deletion.CASCADE, related_name='ecActivity', to='login.todolist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailcheck',
            name='deadline',
            field=models.ForeignKey(default='2199-12-31 23:59:59', on_delete=django.db.models.deletion.CASCADE, related_name='ecDeadline', to='login.todolist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailcheck',
            name='email',
            field=models.ForeignKey(default='default@email.com', on_delete=django.db.models.deletion.CASCADE, related_name='ecEmail', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailcheck',
            name='username',
            field=models.ForeignKey(default='default_username', on_delete=django.db.models.deletion.CASCADE, related_name='ecUname', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]