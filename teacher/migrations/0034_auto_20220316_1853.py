# Generated by Django 3.2.12 on 2022-03-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0033_alter_reportstudent_degree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportstudent',
            name='degree',
        ),
        migrations.AddField(
            model_name='reportstudent',
            name='final_grade',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
