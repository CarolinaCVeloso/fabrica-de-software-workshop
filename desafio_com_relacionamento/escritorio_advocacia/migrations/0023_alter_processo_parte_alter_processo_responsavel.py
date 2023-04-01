# Generated by Django 4.1.7 on 2023-04-01 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio_advocacia', '0022_alter_processo_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='parte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='parte', to='escritorio_advocacia.cliente'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='responsavel', to='escritorio_advocacia.advogado', verbose_name='Responsável'),
        ),
    ]