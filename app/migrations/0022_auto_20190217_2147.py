# Generated by Django 2.1.2 on 2019-02-17 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20190217_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverproducts',
            name='id',
        ),
        migrations.AddField(
            model_name='deliverproducts',
            name='deliver_id',
            field=models.IntegerField(default=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='product',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='deliver_idno',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.DeliverProducts'),
        ),
    ]