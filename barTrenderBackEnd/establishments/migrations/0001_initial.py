# Generated by Django 3.1.4 on 2021-04-02 17:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import establishments.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Bebida', 'B'), ('Estilo', 'E'), ('Instalacion', 'I'), ('Ocio', 'O'), ('Tapa', 'T')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=100)),
                ('cif_text', models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(message='It does not match with CIF pattern.', regex='^[a-zA-Z]{1}\\d{7}[a-zA-Z0-9]{1}$'), establishments.validators.validate_cif])),
                ('phone_number', models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator(message='There have to be 9 numbers.', regex='^\\d{9}$')])),
                ('zone_enum', models.CharField(choices=[('Alameda', 'Al'), ('Triana', 'Tr'), ('Macarena', 'Mc'), ('Remedios', 'Rm'), ('Bermejales', 'B'), ('Cartuja', 'C'), ('Nervion', 'N'), ('San Bernardo', 'Sb'), ('Sevilla Este', 'Se'), ('Bellavista', 'Be'), ('Exterior', 'Ex')], max_length=25)),
                ('verified_bool', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.owner')),
                ('tags', models.ManyToManyField(blank=True, to='establishments.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=50)),
                ('description_text', models.CharField(max_length=140)),
                ('cost_number', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('totalCodes_number', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('scannedCodes_number', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('initial_date', models.DateTimeField(validators=[establishments.validators.date_is_before_now])),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('clients_id', models.ManyToManyField(blank=True, to='authentication.Client')),
                ('establishment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establishments.establishment')),
            ],
        ),
    ]
