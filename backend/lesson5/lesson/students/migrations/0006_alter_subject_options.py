# Generated by Django 4.0.5 on 2022-06-30 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_subject_studentgroup_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
    ]
