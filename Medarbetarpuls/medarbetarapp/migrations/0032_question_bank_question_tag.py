# Generated by Django 5.1.7 on 2025-04-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medarbetarapp', '0031_merge_20250428_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='bank_question_tag',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
