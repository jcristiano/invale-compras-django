# Generated by Django 2.2.14 on 2020-11-22 20:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_compra_itemcompra_local'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='data',
            field=models.DateField(db_column='DT_DATA_COMPRA', default=datetime.datetime(2020, 11, 22, 20, 31, 25, 530160, tzinfo=utc)),
        ),
    ]
