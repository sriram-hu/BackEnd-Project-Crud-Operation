# Generated by Django 5.0.6 on 2024-08-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_duration',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
