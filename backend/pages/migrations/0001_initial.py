# Generated by Django 5.1.7 on 2025-04-07 18:54

import django.db.models.deletion
import pages.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcellFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=pages.models.user_quarter_upload_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'ordering': ['-number'],
            },
        ),
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_name', models.CharField(max_length=255)),
                ('sheet_name_slug', models.CharField(max_length=255)),
                ('csv_path', models.FilePathField(max_length=500)),
                ('quarter_uuid', models.UUIDField(editable=False, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_current', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('quarter_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='csvs', to='pages.excellfile')),
            ],
        ),
        migrations.AddField(
            model_name='excellfile',
            name='quarter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='pages.quarter'),
        ),
    ]
