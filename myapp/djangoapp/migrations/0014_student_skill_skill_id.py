# Generated by Django 2.1.7 on 2019-04-20 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0013_remove_student_skill_skill_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_skill',
            name='skill_id',
            field=models.ManyToManyField(to='djangoapp.Skill'),
        ),
    ]
