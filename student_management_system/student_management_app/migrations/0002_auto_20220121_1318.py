# Generated by Django 3.2.10 on 2022-01-21 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffs',
            old_name='country',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='staffs',
            old_name='gender',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='staffs',
            old_name='phone_number',
            new_name='second_name',
        ),
        migrations.RenameField(
            model_name='staffs',
            old_name='state',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='staffs',
            name='profile_picture',
        ),
    ]
