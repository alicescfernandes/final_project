# Generated by Django 5.1.7 on 2025-04-08 18:12

import pages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_excellfile_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='excellfile',
            name='is_processed',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='excellfile',
            name='file',
            field=models.FileField(max_length=255, upload_to=pages.models.user_quarter_upload_path),
        ),
    ]
