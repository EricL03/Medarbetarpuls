# Generated by Django 5.2 on 2025-04-14 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medarbetarapp', '0002_alter_answer_comment_alter_answer_free_text_answer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SurveyResult',
            new_name='SurveyUserResult',
        ),
    ]
