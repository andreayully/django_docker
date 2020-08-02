# Generated by Django 2.2.14 on 2020-08-01 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del equipo')),
                ('imagen', models.FileField(upload_to='uploads/', verbose_name='Imagen')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('identificacion', models.CharField(max_length=20, verbose_name='identificacion')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Correo electrónico')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioEquipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Equipo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='lider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Usuario'),
        ),
    ]
