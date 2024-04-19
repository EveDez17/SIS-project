# Generated by Django 5.0.4 on 2024-04-19 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_first_name', models.CharField(max_length=100)),
                ('employee_last_name', models.CharField(max_length=100)),
                ('employee_street_number', models.CharField(max_length=128)),
                ('employee_street_name', models.CharField(max_length=255)),
                ('employee_city', models.CharField(max_length=255)),
                ('employee_county', models.CharField(max_length=255)),
                ('employee_country', models.CharField(max_length=255)),
                ('employee_post_code', models.CharField(max_length=20, unique=True)),
                ('date_hired', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_title', models.CharField(max_length=100)),
                ('role_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.employee')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.role')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='user.role'),
        ),
    ]
