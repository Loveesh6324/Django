# Generated by Django 3.2.14 on 2022-11-29 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_alter_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='section',
            field=models.CharField(default=django.utils.timezone.now, max_length=45),
            preserve_default=False,
        ),
    ]
