# Generated by Django 3.2.10 on 2022-04-20 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_alter_subjects_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
