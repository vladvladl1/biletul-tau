# Generated by Django 4.0 on 2022-01-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_eveniment_descriere2_eveniment_pret'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eveniment',
            old_name='Descriere2',
            new_name='Artisti',
        ),
        migrations.AddField(
            model_name='eveniment',
            name='Categorie',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='eveniment',
            name='Data',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
