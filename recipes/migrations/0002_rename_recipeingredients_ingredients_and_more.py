# Generated by Django 4.1 on 2022-08-27 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeIngredients',
            new_name='Ingredients',
        ),
        migrations.RenameField(
            model_name='ingredients',
            old_name='ingredient',
            new_name='product',
        ),
        migrations.AlterModelTable(
            name='ingredients',
            table=None,
        ),
    ]
