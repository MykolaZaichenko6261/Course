# Generated by Django 4.0.5 on 2022-07-01 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_subject_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.subject', verbose_name='Предмет'),
        ),
    ]
