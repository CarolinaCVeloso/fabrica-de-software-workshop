# Generated by Django 4.1.7 on 2023-04-01 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio_advocacia', '0015_processo_parte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processo',
            name='parte',
        ),
    ]