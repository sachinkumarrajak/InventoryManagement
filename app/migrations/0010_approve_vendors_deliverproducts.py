# Generated by Django 2.1.2 on 2019-02-16 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_vendor_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approve_Vendors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('comp_name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=20)),
                ('address', models.TextField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeliverProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('deliver_date', models.DateField()),
                ('tender_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Tender')),
            ],
        ),
    ]
