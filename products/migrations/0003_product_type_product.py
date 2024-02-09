# Generated by Django 5.0.1 on 2024-02-08 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_categoriy_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type_product',
            field=models.CharField(choices=[('FOOD', 'food'), ('DRINK', 'drink')], default=('FOOD', 'food'), max_length=255),
        ),
    ]
