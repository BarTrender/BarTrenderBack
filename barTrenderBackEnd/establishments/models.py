from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from authentication.models import *
from .validators import *
from cloudinary.models import CloudinaryField


# ENUM

class Type(models.TextChoices):
    A = "Ambiente"
    B = "Bebida"
    E = "Estilo"
    I = "Instalacion"
    O = "Ocio"
    T = "Tapa"


class Zone(models.TextChoices):
    AL = "Alameda"
    TR = "Triana"
    MC = "Macarena"
    RM = "Remedios"
    B = "Bermejales"
    C = "Cartuja"
    N = "Nervion"
    SB = "San Bernardo"
    SE = "Sevilla Este"
    BE = "Bellavista"
    EX = "Exterior"


# MODELS

def tags_upload_to(instance, filename):
    return '/'.join(['tags', str(instance.id), filename])


def establishments_upload_to(instance, filename):
    return '/'.join(['establishments', str(instance.id), filename])


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    type = models.CharField(blank=False, null=False, max_length=25, choices=Type.choices)
    photo_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to=tags_upload_to, blank=True, null=True)

    def __str__(self):
        return "Tag: " + self.name + " Type: " + self.type


class Establishment(models.Model):
    name_text = models.CharField(max_length=100, blank=False, null=False)
    desc_text = models.CharField(max_length=200, blank=True, null=True)
    cif_text = models.CharField(max_length=9, blank=False, null=False, unique=True, validators=[
        RegexValidator(
            regex='^[a-zA-Z]{1}\d{7}[a-zA-Z0-9]{1}$',
            message='It does not match with CIF pattern.'
        ),
        validate_cif
    ])
    phone_number = models.IntegerField(blank=False, null=False, unique=True, validators=[
        RegexValidator(
            regex="^\d{9}$",
            message='There have to be 9 numbers.'
        )
    ])
    zone_enum = models.CharField(blank=False, null=False, max_length=25, choices=Zone.choices)
    verified_bool = models.BooleanField(default=False)
    premium_bool = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    street_text = models.CharField(blank=False, null=False, max_length=50)
    number_text = models.CharField(blank=False, null=False, max_length=5)
    locality_text = models.CharField(blank=False, null=False, max_length=50)
    photo_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to=establishments_upload_to, blank=True, null=True)

    def __str__(self):
        return "Establishment: " + self.name_text


class Discount(models.Model):
    name_text = models.CharField(max_length=50, blank=False, null=False)
    description_text = models.CharField(max_length=140)
    cost_number = models.FloatField(blank=False, null=False, default=0.0, validators=[
        MinValueValidator(0.0)
    ])
    totalCodes_number = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    scannedCodes_number = models.PositiveIntegerField(default=0, blank=False, null=False,  validators=[MinValueValidator(0)])
    initial_date = models.DateTimeField(blank=False, null=False, validators=[date_is_before_now])
    end_date = models.DateTimeField(blank=True, null=True)

    # Relations
    clients_id = models.ManyToManyField(Client, blank=True)
    establishment_id = models.ForeignKey(Establishment, on_delete=models.CASCADE)

    def clean(self):
        validate_date(self)
        return self

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Discount, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(Discount, self).save(*args, **kwargs)

    def __str__(self):
        return "Discount: " + self.name_text + "( Id Establecimiento: " + str(self.establishment_id.id) + ")"
