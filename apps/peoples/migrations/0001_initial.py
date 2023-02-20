# Generated by Django 4.1.7 on 2023-02-19 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbPeople',
            fields=[
                ('Id_People', models.AutoField(db_column='Id_People', primary_key=True, serialize=False)),
                ('Id_Username', models.CharField(db_column='Id_Username', max_length=255)),
                ('namePeople', models.CharField(db_column='namePeople', max_length=255)),
                ('emailPeople', models.CharField(db_column='emailPeople', max_length=255)),
                ('phonePeople', models.BigIntegerField(db_column='phonePeople')),
                ('organization', models.ForeignKey(db_column='Id_Organization', on_delete=django.db.models.deletion.CASCADE, to='organizations.tborganization')),
            ],
            options={
                'db_table': 'Tb_People',
                'managed': True,
            },
        ),
    ]