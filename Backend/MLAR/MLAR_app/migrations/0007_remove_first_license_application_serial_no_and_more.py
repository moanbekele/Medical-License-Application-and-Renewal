# Generated by Django 4.2 on 2023-05-06 07:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('MLAR_app', '0006_rename_date_created_first_license_application_date_issued_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='first_license_application',
            name='serial_no',
        ),
        migrations.RemoveField(
            model_name='renew_last_license',
            name='serial_no',
        ),
        migrations.AddField(
            model_name='applicant',
            name='id_serial_no',
            field=models.CharField(default=uuid.uuid4, max_length=36),
        ),
        migrations.AddField(
            model_name='first_license_application',
            name='id_serial_no',
            field=models.CharField(default=uuid.uuid4, max_length=36),
        ),
        migrations.AddField(
            model_name='renew_last_license',
            name='id_serial_no',
            field=models.CharField(default=uuid.uuid4, max_length=36),
        ),
    ]
