# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique_for_date='publish', max_length=200),
        ),
    ]
