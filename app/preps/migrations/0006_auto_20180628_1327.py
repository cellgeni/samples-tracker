# Generated by Django 2.0.6 on 2018-06-28 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preps', '0005_auto_20180628_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='sample_id',
            new_name='sid',
        ),
    ]