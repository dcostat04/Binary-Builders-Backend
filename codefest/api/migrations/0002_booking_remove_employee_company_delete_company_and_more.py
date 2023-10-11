# Generated by Django 4.2.6 on 2023-10-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('referal_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('issue', models.TextField()),
                ('description', models.CharField(max_length=100)),
                ('citizenship_id', models.CharField(max_length=50)),
                ('relation', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]