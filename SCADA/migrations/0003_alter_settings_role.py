# Generated by Django 3.2.5 on 2021-10-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCADA', '0002_settings_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Supervisor', 'Supervisor'), ('Operario', 'Operario')], default='Operario', max_length=10),
        ),
    ]