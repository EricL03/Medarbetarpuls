# Generated by Django 5.1.7 on 2025-04-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medarbetarapp', '0020_merge_20250415_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='is_anonymous',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='is_viewable',
            field=models.BooleanField(default=True),
        ),
    ]
