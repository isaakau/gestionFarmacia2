# Generated by Django 3.2.3 on 2022-05-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_auto_20220515_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='idLab',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='codigo',
            field=models.AutoField(max_length=99999999, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='receta',
            name='idReceta',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='idReserva',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
