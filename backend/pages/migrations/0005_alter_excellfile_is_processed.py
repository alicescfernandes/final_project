# Generated by Django 5.1.7 on 2025-04-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_excellfile_is_processed_alter_excellfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excellfile',
            name='is_processed',
            field=models.BooleanField(default=False),
        ),
    ]
