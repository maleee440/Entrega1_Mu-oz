# Generated by Django 4.1.1 on 2022-09-25 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSuper', '0009_producto_camada'),
    ]

    operations = [
        migrations.AddField(
            model_name='cajero',
            name='apellido',
            field=models.CharField(default=45, max_length=60),
            preserve_default=False,
        ),
    ]