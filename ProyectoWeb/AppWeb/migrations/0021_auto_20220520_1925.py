# Generated by Django 3.0.7 on 2022-05-20 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0020_rename_nombremedicamento_medicamento_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='medicamentoRecetado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppWeb.Medicamento', verbose_name='Medicamento'),
        ),
        migrations.AlterField(
            model_name='retiro',
            name='medicamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppWeb.Medicamento'),
        ),
    ]
