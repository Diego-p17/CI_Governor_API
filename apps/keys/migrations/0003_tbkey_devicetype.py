# Generated by Django 4.1.7 on 2023-02-23 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generals', '0001_initial'),
        ('keys', '0002_tbkey_valuekey'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbkey',
            name='deviceType',
            field=models.ForeignKey(db_column='Id_DeviceType', default=2, on_delete=django.db.models.deletion.CASCADE, to='generals.tbdevicetype'),
            preserve_default=False,
        ),
    ]
