# Generated by Django 5.0.7 on 2024-07-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_api', '0002_alter_recipes_popularity'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='description',
            field=models.TextField(default='default description'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='images',
            field=models.TextField(default='default image url'),
        ),
    ]