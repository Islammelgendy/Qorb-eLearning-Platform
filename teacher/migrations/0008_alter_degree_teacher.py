# Generated by Django 3.2.12 on 2022-02-17 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('teacher', '0007_degree_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='teacher',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher'),
        ),
    ]
