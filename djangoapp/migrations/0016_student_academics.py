# Generated by Django 2.1.7 on 2019-04-20 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0015_student_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Academics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_number', models.BigIntegerField()),
                ('graduated', models.BooleanField()),
                ('graduated_on', models.DateField()),
                ('major', models.CharField(max_length=20)),
                ('university_name', models.TextField(max_length=50)),
                ('CGPA', models.DecimalField(decimal_places=2, max_digits=4)),
                ('student_id', models.ForeignKey(on_delete='CASCADE', to='djangoapp.Student')),
            ],
        ),
    ]
