# Generated by Django 4.0.4 on 2022-04-20 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField()),
                ('bname', models.CharField(max_length=100)),
                ('bauthor', models.CharField(max_length=100)),
                ('bqty', models.IntegerField()),
            ],
        ),
    ]
