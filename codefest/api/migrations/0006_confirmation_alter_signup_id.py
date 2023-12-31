# Generated by Django 4.2.6 on 2023-10-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_merge_0004_booking_city_0004_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('issue', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='signup',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
