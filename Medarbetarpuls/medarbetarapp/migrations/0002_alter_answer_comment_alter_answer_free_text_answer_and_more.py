# Generated by Django 5.2 on 2025-04-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medarbetarapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='free_text_answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='multiple_choice_answer',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='slider_answer',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='yes_no_answer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
