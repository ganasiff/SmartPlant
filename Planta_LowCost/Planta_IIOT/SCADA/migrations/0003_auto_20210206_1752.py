# Generated by Django 3.1.2 on 2021-02-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCADA', '0002_transmisoresp_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transmisoresp',
            name='esp_ai_channel',
        ),
        migrations.AddField(
            model_name='transmisoresp',
            name='datapoint',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
