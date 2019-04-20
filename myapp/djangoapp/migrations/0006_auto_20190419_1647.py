# Generated by Django 2.1.7 on 2019-04-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_auto_20190419_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_language',
            name='read_language',
            field=models.ManyToManyField(related_name='read_language', to='djangoapp.Language'),
        ),
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
