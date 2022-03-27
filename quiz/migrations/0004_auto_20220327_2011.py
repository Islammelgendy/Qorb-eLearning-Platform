# Generated by Django 3.2.5 on 2022-03-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20220312_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizstudent',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='quizstudent',
            name='total_marks',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='correct',
            field=models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], max_length=200),
        ),
    ]