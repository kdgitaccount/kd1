# Generated by Django 4.1.5 on 2023-01-16 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=1000)),
                ('experience', models.IntegerField()),
                ('contact', models.CharField(max_length=1000)),
            ],
        ),
    ]
