# Generated by Django 5.1.7 on 2025-03-30 16:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medarbetarapp', '0004_rename_role_customuser_userrole_customuser_admin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('deadline', models.DateTimeField()),
                ('sending_date', models.DateTimeField()),
                ('collectedAnswerCount', models.IntegerField(default=0)),
                ('isViewable', models.BooleanField(default=False)),
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('employeeGroups', models.ManyToManyField(related_name='publishedSurveys', to='medarbetarapp.employeegroup')),
            ],
        ),
    ]
