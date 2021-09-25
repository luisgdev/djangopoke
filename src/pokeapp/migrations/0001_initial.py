# Generated by Django 3.2.7 on 2021-09-25 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('poke_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('base_stat', models.IntegerField()),
                ('effort', models.IntegerField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokeapp.pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='Evolution',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('evo_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('evo_type', models.CharField(max_length=64)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokeapp.pokemon')),
            ],
        ),
    ]
