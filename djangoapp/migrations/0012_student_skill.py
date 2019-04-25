# Generated by Django 2.1.7 on 2019-04-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0011_auto_20190420_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_proficiency', models.CharField(choices=[('', ''), ('good', 'Good'), ('average', 'Average'), ('excellent', 'Excellent'), ('poor', 'Poor')], max_length=10)),
                ('experience', models.SlugField()),
                ('skill_id', models.ForeignKey(on_delete='CASCADE', to='djangoapp.Skill')),
                ('student_id', models.ForeignKey(on_delete='CASCADE', to='djangoapp.Student')),
            ],
        ),
    ]