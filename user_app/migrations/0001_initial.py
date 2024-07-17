# Generated by Django 5.0.6 on 2024-07-17 08:50

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderFood',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_app.food')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('o_id', models.UUIDField(default=uuid.uuid4)),
                ('del_charge', models.IntegerField(default=20)),
                ('total_amount', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_app.hotel')),
                ('o_food', models.ManyToManyField(to='user_app.orderfood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'CartItem',
            },
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('mobile', models.IntegerField()),
                ('country', models.CharField(max_length=250)),
                ('zip', models.IntegerField()),
                ('notes', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('order placed', 'order placed'), ('hotel done', 'hotel done'), ('out for delivery', 'out for delivery'), ('delivery compleated', 'delivery compleated')], default=('pending', 'pending'), max_length=250)),
                ('payment_type', models.CharField(choices=[('online pay', 'online pay'), ('COD', 'COD')], max_length=250)),
                ('payment', models.BooleanField(default=False)),
                ('delivery_b', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.orderfood')),
            ],
        ),
    ]
