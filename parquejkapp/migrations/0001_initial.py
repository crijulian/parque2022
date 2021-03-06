# Generated by Django 4.0 on 2021-12-28 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plazas',
            fields=[
                ('idplazas', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_plaza', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=30)),
                ('tipo_vehiculo', models.CharField(max_length=30)),
                ('fecha_entrada', models.DateTimeField()),
                ('id_plazask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facidplazas', to='parquejkapp.plazas')),
            ],
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('idfactura', models.AutoField(primary_key=True, serialize=False)),
                ('costo_total', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fecha_salida', models.DateTimeField()),
                ('ususariok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factuiduser', to='parquejkapp.user')),
            ],
        ),
    ]
