# Generated by Django 4.0 on 2022-01-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_eveniment'),
    ]

    operations = [
        migrations.AddField(
            model_name='eveniment',
            name='Descriere2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='eveniment',
            name='Pret',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
