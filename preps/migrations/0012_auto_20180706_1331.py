# Generated by Django 2.0.6 on 2018-07-06 13:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('preps', '0011_auto_20180706_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
