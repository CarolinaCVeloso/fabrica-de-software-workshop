# Generated by Django 4.1.7 on 2023-03-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogame_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=12)),
            ],
        ),
    ]
