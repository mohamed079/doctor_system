# Generated by Django 4.1 on 2022-10-19 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservation', '0001_initial'),
        ('patient', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='doctor.doctor'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='patient.patient'),
        ),
    ]
