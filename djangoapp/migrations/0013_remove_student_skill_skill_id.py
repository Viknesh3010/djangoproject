# Generated by Django 2.1.7 on 2019-04-20 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0012_student_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_skill',
            name='skill_id',
        ),
    ]
