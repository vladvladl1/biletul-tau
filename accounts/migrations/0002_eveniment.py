# Generated by Django 4.0 on 2022-01-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eveniment',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Nume', models.CharField(max_length=255, null=True)),
                ('Descriere', models.CharField(max_length=255, null=True)),
                ('Oras', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
