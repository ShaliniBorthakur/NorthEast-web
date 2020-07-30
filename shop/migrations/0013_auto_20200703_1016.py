# Generated by Django 2.2 on 2020-07-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_product_quantity_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('TEX', 'Textile'), ('HAN', 'Handicraft')], default='TEX', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(choices=[('ASS', 'Assam'), ('MAN', 'Manipur'), ('ARU', 'Arunachal Pradesh'), ('TRI', 'Tripura'), ('SIK', 'Sikkim'), ('NAG', 'Nagaland'), ('MEG', 'Meghalaya'), ('MIZ', 'Mizoram')], default='ASS', max_length=50),
        ),
    ]
