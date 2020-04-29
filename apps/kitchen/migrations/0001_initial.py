# Generated by Django 3.0.5 on 2020-04-29 03:46

import datetime
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
            name='Combo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'combo',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ingredient',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Fecha')),
                ('combo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.Combo')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('combo', models.ManyToManyField(to='kitchen.Combo')),
            ],
            options={
                'db_table': 'menu',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('type_f', models.CharField(max_length=50)),
                ('exceptions', models.ManyToManyField(blank=True, to='kitchen.Ingredient')),
            ],
            options={
                'db_table': 'food',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='combo',
            name='food',
            field=models.ManyToManyField(to='kitchen.Food'),
        ),
    ]