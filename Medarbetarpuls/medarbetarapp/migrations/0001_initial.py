# Generated by Django 5.2 on 2025-04-10 10:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_format', models.CharField(choices=[('multiplechoice', 'Multiple choice'), ('yesno', 'Yes No'), ('text', 'Text'), ('slider', 'Slider')], default='multiplechoice', max_length=15)),
                ('options', models.JSONField(default=list)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SliderQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_format', models.CharField(choices=[('multiplechoice', 'Multiple choice'), ('yesno', 'Yes No'), ('text', 'Text'), ('slider', 'Slider')], default='slider', max_length=15)),
                ('max_interval', models.IntegerField(default=10)),
                ('min_interval', models.IntegerField(default=0)),
                ('max_text', models.CharField(max_length=255)),
                ('min_text', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_format', models.CharField(choices=[('multiplechoice', 'Multiple choice'), ('yesno', 'Yes No'), ('text', 'Text'), ('slider', 'Slider')], default='text', max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YesNoQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_format', models.CharField(choices=[('multiplechoice', 'Multiple choice'), ('yesno', 'Yes No'), ('text', 'Text'), ('slider', 'Slider')], default='yesno', max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_groups', to='medarbetarapp.organization')),
            ],
        ),
        migrations.CreateModel(
            name='EmailList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_emails', to='medarbetarapp.organization')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('user_role', models.CharField(choices=[('admin', 'Admin'), ('surveycreator', 'SurveyCreator'), ('surveyresponder', 'SurveyResponder')], default='surveyresponder', max_length=15)),
                ('authorization_level', models.IntegerField(default=0)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('employee_groups', models.ManyToManyField(related_name='employees', to='medarbetarapp.employeegroup')),
                ('survey_groups', models.ManyToManyField(related_name='managers', to='medarbetarapp.employeegroup')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admins', to='medarbetarapp.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('deadline', models.DateTimeField()),
                ('sending_date', models.DateTimeField()),
                ('collected_answer_count', models.IntegerField(default=0)),
                ('is_viewable', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='published_surveys', to=settings.AUTH_USER_MODEL)),
                ('employee_groups', models.ManyToManyField(related_name='+', to='medarbetarapp.employeegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('question_format', models.CharField(choices=[('multiplechoice', 'Multiple choice'), ('yesno', 'Yes No'), ('text', 'Text'), ('slider', 'Slider')], default='text', max_length=15)),
                ('question_type', models.CharField(choices=[('onetime', 'Onetime'), ('reoccurring', 'Reoccurring'), ('builtin', 'Built in'), ('enps', 'ENPS')], default='onetime', max_length=15)),
                ('bank_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_bank', to='medarbetarapp.organization')),
                ('multiple_choice_question', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medarbetarapp.multiplechoicequestion')),
                ('slider_question', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medarbetarapp.sliderquestion')),
                ('connected_surveys', models.ManyToManyField(related_name='questions', to='medarbetarapp.survey')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_answered', models.BooleanField(default=False)),
                ('published_survey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_results', to='medarbetarapp.survey')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_results', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_answered', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=255)),
                ('free_text_answer', models.CharField(max_length=255)),
                ('multiple_choice_answer', models.JSONField(default=list)),
                ('yes_no_answer', models.BooleanField(default=False)),
                ('slider_answer', models.FloatField()),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='medarbetarapp.question')),
                ('survey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='medarbetarapp.surveyresult')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_edited', models.DateTimeField()),
                ('bank_survey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_template_bank', to='medarbetarapp.organization')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_templates', to=settings.AUTH_USER_MODEL)),
                ('employee_groups', models.ManyToManyField(related_name='+', to='medarbetarapp.employeegroup')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey_template',
            field=models.ManyToManyField(related_name='questions', to='medarbetarapp.surveytemplate'),
        ),
        migrations.AddField(
            model_name='question',
            name='text_question',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medarbetarapp.textquestion'),
        ),
        migrations.AddField(
            model_name='question',
            name='yes_no_question',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medarbetarapp.yesnoquestion'),
        ),
    ]
