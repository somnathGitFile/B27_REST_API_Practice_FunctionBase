# Generated by Django 4.0.4 on 2022-04-20 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adharcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.IntegerField()),
                ('aname', models.CharField(max_length=100)),
                ('anumber', models.IntegerField()),
                ('aadd', models.CharField(max_length=200)),
            ],
        ),
    ]
