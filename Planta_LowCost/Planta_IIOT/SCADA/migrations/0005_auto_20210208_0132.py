# Generated by Django 3.1.2 on 2021-02-08 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCADA', '0004_datapoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='channel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='tag',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='transmisor',
            field=models.CharField(default='', max_length=200),
        ),
    ]