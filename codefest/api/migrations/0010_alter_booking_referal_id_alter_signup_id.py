# Generated by Django 4.2.6 on 2023-10-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_booking_referal_id_alter_signup_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='referal_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='signup',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
