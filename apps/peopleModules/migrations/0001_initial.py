# Generated by Django 4.1.7 on 2023-03-03 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('peoples', '0001_initial'),
        ('aplications', '0002_tbaplication_isactive'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbPeopleModule',
            fields=[
                ('Id_PeopleModule', models.AutoField(db_column='Id_PackageConfigKeys', primary_key=True, serialize=False)),
                ('valueModule', models.TextField(db_column='valueModule')),
                ('module', models.ForeignKey(db_column='Id_Module', on_delete=django.db.models.deletion.CASCADE, to='aplications.tbmodule')),
                ('people', models.ForeignKey(db_column='Id_People', on_delete=django.db.models.deletion.CASCADE, to='peoples.tbpeople')),
            ],
            options={
                'db_table': 'Tb_PeopleModule',
                'managed': True,
            },
        ),
    ]