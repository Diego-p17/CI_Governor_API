# Generated by Django 4.1.7 on 2023-02-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbsetting',
            name='nameSetting',
            field=models.CharField(db_column='nameSetting', default=1, max_length=255),
            preserve_default=False,
        ),
    ]
