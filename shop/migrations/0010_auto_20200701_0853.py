# Generated by Django 2.2 on 2020-07-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
