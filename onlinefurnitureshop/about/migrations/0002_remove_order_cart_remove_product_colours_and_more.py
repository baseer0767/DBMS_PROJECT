# Generated by Django 5.0.6 on 2024-06-30 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='product',
            name='colours',
        ),
        migrations.RemoveField(
            model_name='order',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Colour',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
