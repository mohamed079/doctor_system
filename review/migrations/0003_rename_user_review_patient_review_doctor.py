# Generated by Django 4.1 on 2022-10-21 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('review', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='patient',
        ),
        migrations.AddField(
            model_name='review',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='doctor.doctor'),
        ),
    ]