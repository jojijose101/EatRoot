# Generated by Django 5.0.6 on 2024-07-22 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_alter_orderitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.orderitem'),
        ),
    ]