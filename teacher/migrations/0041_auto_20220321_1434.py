# Generated by Django 3.2.12 on 2022-03-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0040_alter_report_student_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report_student',
            old_name='notes',
            new_name='student_notes',
        ),
        migrations.AddField(
            model_name='report_student',
            name='teacher_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
