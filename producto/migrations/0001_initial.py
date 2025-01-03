# Generated by Django 4.2.17 on 2024-12-25 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad en stock')),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio unitario')),
                ('fecha_ingreso', models.DateField(auto_now_add=True, verbose_name='Fecha de ingreso')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha_prestamo', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos_realizados', to=settings.AUTH_USER_MODEL)),
                ('usuario_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prestamos_recibidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('leida', models.BooleanField(default=False)),
                ('aprobada', models.BooleanField(default=False)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aprobada', 'Aprobada'), ('Rechazada', 'Rechazada')], default='Pendiente', max_length=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
