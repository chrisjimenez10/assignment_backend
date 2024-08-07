# Generated by Django 5.0.7 on 2024-07-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('main_ingredient', models.CharField(max_length=32)),
                ('origin', models.CharField(max_length=32)),
                ('popularity', models.IntegerField()),
            ],
        ),
    ]
