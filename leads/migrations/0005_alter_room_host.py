# Generated by Django 3.2.7 on 2021-09-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_alter_room_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
