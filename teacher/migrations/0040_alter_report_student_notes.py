# Generated by Django 3.2.12 on 2022-03-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0039_auto_20220321_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_student',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
