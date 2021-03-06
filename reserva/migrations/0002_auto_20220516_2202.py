# Generated by Django 3.2.3 on 2022-05-17 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamento',
            name='reservado',
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('idReserva', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadReservada', models.IntegerField()),
                ('codMed', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='reserva.medicamento')),
                ('idDetalle', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='reserva.detallereceta')),
                ('rutPaciente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='reserva.paciente')),
            ],
        ),
    ]
