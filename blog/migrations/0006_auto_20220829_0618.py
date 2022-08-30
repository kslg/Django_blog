# Generated by Django 3.2.15 on 2022-08-29 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_appointment_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='color',
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.CharField(choices=[('0', '15:30 - 15:45'), ('1', '15:45 - 16:00'), ('2', '16:00 - 16:15'), ('3', '16:15 - 16:30'), ('4', '16:30 - 16:45'), ('5', '16:45 - 17:00')], default='0', max_length=6),
        ),
    ]