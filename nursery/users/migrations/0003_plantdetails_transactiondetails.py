# Generated by Django 2.2.2 on 2020-12-20 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201220_0420'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantDetails',
            fields=[
                ('plant_id', models.IntegerField(primary_key=True, serialize=False)),
                ('plant_name', models.CharField(max_length=40)),
                ('plant_count', models.IntegerField(default=0)),
                ('plant_info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('txn_id', models.IntegerField(primary_key=True, serialize=False)),
                ('txn_amount', models.FloatField()),
                ('txn_date', models.DateTimeField()),
                ('plant_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.PlantDetails')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
