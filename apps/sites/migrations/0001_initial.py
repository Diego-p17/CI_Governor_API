# Generated by Django 4.1.7 on 2023-02-19 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
        ('generals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbSite',
            fields=[
                ('Id_Site', models.AutoField(db_column='Id_Site', primary_key=True, serialize=False)),
                ('nameSite', models.CharField(db_column='nameSite', max_length=255)),
                ('addressSite', models.CharField(db_column='addressSite', max_length=255)),
                ('isActive', models.BooleanField(db_column='isActive', default=True)),
                ('city', models.ForeignKey(db_column='Id_City', on_delete=django.db.models.deletion.CASCADE, to='generals.tbcity')),
                ('organization', models.ForeignKey(db_column='Id_Organization', on_delete=django.db.models.deletion.CASCADE, to='organizations.tborganization')),
            ],
            options={
                'db_table': 'Tb_Site',
                'managed': True,
            },
        ),
    ]