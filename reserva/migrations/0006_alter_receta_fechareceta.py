# Generated by Django 3.2.3 on 2022-05-15 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0005_auto_20220515_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='fechaReceta',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
