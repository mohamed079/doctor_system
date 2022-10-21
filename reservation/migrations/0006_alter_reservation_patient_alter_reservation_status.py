# Generated by Django 4.1 on 2022-10-20 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0005_alter_reservation_patient_alter_reservation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Acceptance', 'Acceptance'), ('Rejected', 'Rejected')], default='Pending', max_length=15),
        ),
    ]
