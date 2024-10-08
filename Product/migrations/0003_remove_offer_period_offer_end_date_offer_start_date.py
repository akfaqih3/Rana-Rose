# Generated by Django 5.0.6 on 2024-07-02 15:14

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_alter_category_photo_alter_product_photo_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='period',
        ),
        migrations.AddField(
            model_name='offer',
            name='end_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='offer',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
