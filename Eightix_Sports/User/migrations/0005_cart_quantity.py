# Generated by Django 3.2.14 on 2022-11-16 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
