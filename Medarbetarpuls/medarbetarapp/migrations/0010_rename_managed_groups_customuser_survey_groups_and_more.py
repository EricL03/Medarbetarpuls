# Generated by Django 5.1.7 on 2025-04-01 14:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medarbetarapp', '0009_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='managed_groups',
            new_name='survey_groups',
        ),
        migrations.AddField(
            model_name='surveyresult',
            name='answered_users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answered_surveys', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='surveyresult',
            name='un_answered_users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='un_answered_surveys', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='surveytemplate',
            name='bank_survey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_template_bank', to='medarbetarapp.organization'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('question_format', models.CharField(choices=[('multiplechoice', 'MultipleChoice'), ('yesno', 'YesNo'), ('text', 'Text'), ('slider', 'Slider')], default='text', max_length=15)),
                ('question_type', models.CharField(choices=[('onetime', 'Onetime'), ('reoccurring', 'Reoccurring'), ('builtin', 'Builtin'), ('enps', 'ENPS')], default='onetime', max_length=15)),
                ('bank_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_bank', to='medarbetarapp.organization')),
                ('connected_surveys', models.ManyToManyField(related_name='questions', to='medarbetarapp.survey')),
                ('survey_template', models.ManyToManyField(related_name='questions', to='medarbetarapp.surveytemplate')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='medarbetarapp.question'),
            preserve_default=False,
        ),
    ]
