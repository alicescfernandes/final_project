# Generated by Django 5.1.7 on 2025-04-08 18:20

import pages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_excellfile_is_processed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excellfile',
            name='file',
            field=models.FileField(upload_to=pages.models.user_quarter_upload_path),
        ),
    ]
