# Generated by Django 3.2.7 on 2021-09-28 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_rename_livro_model_bibliotecamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bibliotecamodel',
            name='ano_publicacao',
            field=models.IntegerField(blank=True, max_length=4),
        ),
    ]
