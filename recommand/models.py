from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class WineFirst(models.Model):
    origin_index = models.IntegerField(default=0)
    country = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    designation = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    province = models.CharField(max_length=50)
    taster_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
    winery = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    aging = models.CharField(max_length=50)

    class Meta:
        db_table = 'wine1st'


class WineSecond(models.Model):
    origin_index = models.IntegerField(default=0)
    country = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    designation = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    province = models.CharField(max_length=50)
    taster_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
    winery = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    aging = models.CharField(max_length=50)

    class Meta:
        db_table = 'wine2nd'


class WineThird(models.Model):
    origin_index = models.IntegerField(default=0)
    country = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    designation = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    province = models.CharField(max_length=50)
    taster_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
    winery = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    aging = models.CharField(max_length=50)

    class Meta:
        db_table = 'wine3rd'


class CosFirst(models.Model):
    recommand_1 = models.IntegerField(default=0)
    recommand_2 = models.IntegerField(default=0)
    recommand_3 = models.IntegerField(default=0)

    class Meta:
        db_table = 'cos1st'


class CosSecond(models.Model):
    recommand_1 = models.IntegerField(default=0)
    recommand_2 = models.IntegerField(default=0)
    recommand_3 = models.IntegerField(default=0)

    class Meta:
        db_table = 'cos2nd'


class CosThird(models.Model):
    recommand_1 = models.IntegerField(default=0)
    recommand_2 = models.IntegerField(default=0)
    recommand_3 = models.IntegerField(default=0)

    class Meta:
        db_table = 'cos3rd'
