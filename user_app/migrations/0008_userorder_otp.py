# Generated by Django 5.0.6 on 2024-07-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_alter_userorder_payment_type_alter_userorder_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
