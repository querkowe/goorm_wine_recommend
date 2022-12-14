# Generated by Django 3.2 on 2022-10-28 08:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CosFirst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommand_1', models.IntegerField(default=0)),
                ('recommand_2', models.IntegerField(default=0)),
                ('recommand_3', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'cos1st',
            },
        ),
        migrations.CreateModel(
            name='CosSecond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommand_1', models.IntegerField(default=0)),
                ('recommand_2', models.IntegerField(default=0)),
                ('recommand_3', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'cos2nd',
            },
        ),
        migrations.CreateModel(
            name='CosThird',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommand_1', models.IntegerField(default=0)),
                ('recommand_2', models.IntegerField(default=0)),
                ('recommand_3', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'cos3rd',
            },
        ),
        migrations.CreateModel(
            name='ImageSrc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_index', models.IntegerField(default=0)),
                ('src', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'imgsrc',
            },
        ),
        migrations.CreateModel(
            name='WineFirst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_index', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=800)),
                ('designation', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('province', models.CharField(max_length=50)),
                ('taster_name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=150)),
                ('variety', models.CharField(max_length=50)),
                ('winery', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=0)),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('aging', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'wine1st',
            },
        ),
        migrations.CreateModel(
            name='WineName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_index', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=150)),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
            ],
            options={
                'db_table': 'winename',
            },
        ),
        migrations.CreateModel(
            name='WineSecond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_index', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=800)),
                ('designation', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('province', models.CharField(max_length=50)),
                ('taster_name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=150)),
                ('variety', models.CharField(max_length=50)),
                ('winery', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=0)),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('aging', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'wine2nd',
            },
        ),
        migrations.CreateModel(
            name='WineThird',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_index', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=800)),
                ('designation', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('province', models.CharField(max_length=50)),
                ('taster_name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=150)),
                ('variety', models.CharField(max_length=50)),
                ('winery', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=0)),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('aging', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'wine3rd',
            },
        ),
    ]
