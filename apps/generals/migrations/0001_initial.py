# Generated by Django 4.1.7 on 2023-02-19 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbCountry',
            fields=[
                ('Id_Country', models.AutoField(db_column='Id_Country', primary_key=True, serialize=False)),
                ('nameCountry', models.CharField(db_column='nameCountry', max_length=255)),
            ],
            options={
                'db_table': 'Tb_Country',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbDeviceType',
            fields=[
                ('Id_DeviceType', models.AutoField(db_column='Id_DeviceType', primary_key=True, serialize=False)),
                ('nameDeviceType', models.CharField(db_column='nameDeviceType', max_length=255)),
            ],
            options={
                'db_table': 'Tb_DeviceType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbHwPlatform',
            fields=[
                ('Id_HwPlatform', models.AutoField(db_column='Id_HwPlatform', primary_key=True, serialize=False)),
                ('nameHwPlatform', models.CharField(db_column='nameHwPlatform', max_length=255)),
            ],
            options={
                'db_table': 'Tb_HwPlatform',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbLevelKeys',
            fields=[
                ('Id_LevelKeys', models.AutoField(db_column='Id_TokenType', primary_key=True, serialize=False)),
                ('nameLevelKeys', models.CharField(db_column='nameLevelKeys', max_length=255)),
            ],
            options={
                'db_table': 'Tb_LevelKeys',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbOs',
            fields=[
                ('Id_Os', models.AutoField(db_column='Id_Os', primary_key=True, serialize=False)),
                ('nameOs', models.CharField(db_column='nameOs', max_length=255)),
            ],
            options={
                'db_table': 'Tb_Os',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbSettingType',
            fields=[
                ('Id_SettingType', models.AutoField(db_column='Id_SettingType', primary_key=True, serialize=False)),
                ('nameSettingType', models.CharField(db_column='nameSettingType', max_length=255)),
            ],
            options={
                'db_table': 'Tb_SettingType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbTokenType',
            fields=[
                ('Id_TokenType', models.AutoField(db_column='Id_TokenType', primary_key=True, serialize=False)),
                ('nameTokenType', models.CharField(db_column='nameTokenType', max_length=255)),
            ],
            options={
                'db_table': 'Tb_TokenType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbCity',
            fields=[
                ('Id_City', models.AutoField(db_column='Id_City', primary_key=True, serialize=False)),
                ('nameCity', models.CharField(db_column='nameCity', max_length=255)),
                ('country', models.ForeignKey(db_column='Id_Country', on_delete=django.db.models.deletion.CASCADE, to='generals.tbcountry')),
            ],
            options={
                'db_table': 'Tb_City',
                'managed': True,
            },
        ),
    ]
