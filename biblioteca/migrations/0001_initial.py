# Generated by Django 3.2.7 on 2021-09-28 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_livro', models.CharField(blank=True, max_length=255)),
                ('isbn', models.CharField(blank=True, max_length=13)),
                ('autor', models.CharField(max_length=255)),
                ('ano_publicacao', models.DateField(blank=True)),
                ('genero', models.CharField(max_length=255)),
                ('idioma', models.CharField(max_length=20)),
            ],
        ),
    ]
