# Generated by Django 5.0.6 on 2024-05-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_mgmt', '0004_alter_employee_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
