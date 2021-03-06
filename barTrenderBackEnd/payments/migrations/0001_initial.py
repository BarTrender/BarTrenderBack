# Generated by Django 3.1.4 on 2021-04-28 19:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField(blank=True, null=True)),
                ('scanned_number', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('discount_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='establishments.discount')),
            ],
        ),
    ]
