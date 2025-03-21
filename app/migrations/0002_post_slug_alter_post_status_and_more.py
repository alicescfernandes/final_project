# Generated by Django 5.1.7 on 2025-03-21 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')], default='draft', max_length=10),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['created_date'], name='app_post_created_ddea7d_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['status'], name='app_post_status_3d3324_idx'),
        ),
    ]
