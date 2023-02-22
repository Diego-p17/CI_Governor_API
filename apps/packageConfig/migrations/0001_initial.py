# Generated by Django 4.1.7 on 2023-02-22 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('generals', '0001_initial'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbPackageConfig',
            fields=[
                ('Id_PackageConfig', models.AutoField(db_column='Id_PackageConfig', primary_key=True, serialize=False)),
                ('namePackage', models.TextField(db_column='namePackage')),
                ('site', models.IntegerField(db_column='Id_Site', default=0, null=True)),
                ('zone', models.IntegerField(db_column='Id_Zone', default=0, null=True)),
                ('deviceType', models.ForeignKey(db_column='Id_DeviceType', on_delete=django.db.models.deletion.CASCADE, to='generals.tbdevicetype')),
                ('organization', models.ForeignKey(db_column='Id_Organization', on_delete=django.db.models.deletion.CASCADE, to='organizations.tborganization')),
            ],
            options={
                'db_table': 'Tb_PackageConfig',
                'managed': True,
            },
        ),
    ]
