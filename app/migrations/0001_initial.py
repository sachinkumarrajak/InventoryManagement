# Generated by Django 2.1.2 on 2019-02-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginDetails',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Admin', 'admin'), ('Area Manager', 'area manager'), ('Analyzer', 'analyzer'), ('Vendor', 'vendor')], max_length=30)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
    ]
