# Generated by Django 4.1.7 on 2023-04-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio_advocacia', '0022_alter_processo_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='parte',
            field=models.CharField(max_length=100),
        ),
    ]
