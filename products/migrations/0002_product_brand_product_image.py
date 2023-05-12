# Generated by Django 4.2 on 2023-05-12 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_brand'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='common.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]
