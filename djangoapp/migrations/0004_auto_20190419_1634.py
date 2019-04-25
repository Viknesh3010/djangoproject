# Generated by Django 2.1.7 on 2019-04-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_delete_candidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_language',
            name='speak_language',
            field=models.ManyToManyField(related_name='speak_language', to='djangoapp.Language'),
        ),
        migrations.AddField(
            model_name='student_language',
            name='write_language',
            field=models.ManyToManyField(related_name='write_language', to='djangoapp.Language'),
        ),
    ]
