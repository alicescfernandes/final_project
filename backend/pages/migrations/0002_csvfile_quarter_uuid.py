# Generated by Django 5.1.7 on 2025-04-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfile',
            name='quarter_uuid',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
