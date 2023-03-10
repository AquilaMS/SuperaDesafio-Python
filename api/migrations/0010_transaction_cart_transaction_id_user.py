# Generated by Django 4.1.6 on 2023-02-10 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_cart_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='cart',
            field=models.ManyToManyField(to='api.cart'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='id_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
