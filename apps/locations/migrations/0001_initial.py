# Generated by Django 4.1.7 on 2023-02-19 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0001_initial'),
        ('devices', '0001_initial'),
        ('zones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbLocation',
            fields=[
                ('Id_Location', models.AutoField(db_column='Id_Location', primary_key=True, serialize=False)),
                ('addressLocation', models.CharField(db_column='addressLocation', max_length=255)),
                ('isActive', models.BooleanField(db_column='isActive', default=True)),
                ('device', models.ForeignKey(db_column='Id_Device', on_delete=django.db.models.deletion.CASCADE, to='devices.tbdevice')),
                ('site', models.ForeignKey(db_column='Id_Site', on_delete=django.db.models.deletion.CASCADE, to='sites.tbsite')),
                ('zone', models.ForeignKey(db_column='Id_Zone', on_delete=django.db.models.deletion.CASCADE, to='zones.tbzone')),
            ],
        ),
    ]
