# Generated by Django 2.1.2 on 2019-02-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190217_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverproducts',
            name='tender_id',
            field=models.IntegerField(),
        ),
    ]
