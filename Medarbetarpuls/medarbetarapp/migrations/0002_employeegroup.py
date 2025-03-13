# Generated by Django 5.1.7 on 2025-03-13 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medarbetarapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employeeGroups', to='medarbetarapp.organization')),
            ],
        ),
    ]
