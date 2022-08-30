# Generated by Django 3.2.15 on 2022-08-29 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6),
        ),
    ]