# Generated by Django 5.0.7 on 2024-08-07 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='working_hours',
            field=models.CharField(choices=[('07:00-15:00', 'Morning (07:00-15:00)'), ('15:00-23:00', 'Evening (15:00-23:00)')], max_length=11),
        ),
    ]