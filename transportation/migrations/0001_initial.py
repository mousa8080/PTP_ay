# Generated by Django 5.1.6 on 2025-03-14 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_point', models.CharField(max_length=255)),
                ('end_point', models.CharField(max_length=255)),
                ('total_distance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('estimated_time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=255)),
                ('password_hash', models.TextField()),
                ('user_type', models.CharField(choices=[('passenger', 'Passenger'), ('driver', 'Driver'), ('admin', 'Admin')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('under_review', 'Under Review'), ('resolved', 'Resolved')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_reports', to='transportation.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reports', to='transportation.user')),
            ],
        ),
        migrations.CreateModel(
            name='DriverEarnings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid')], max_length=10)),
                ('confirmed_at', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(limit_choices_to={'user_type': 'driver'}, on_delete=django.db.models.deletion.CASCADE, to='transportation.user')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=50)),
                ('gps_enabled', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(limit_choices_to={'user_type': 'driver'}, on_delete=django.db.models.deletion.CASCADE, to='transportation.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare', models.DecimalField(decimal_places=2, max_digits=5)),
                ('payment_method', models.CharField(choices=[('NC', 'Non-Cash'), ('QR', 'QR Payment')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportation.user')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportation.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportation.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transportation.user')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_type', models.CharField(choices=[('fare_payment', 'Fare Payment'), ('wallet_topup', 'Wallet Top-up'), ('transfer', 'Transfer')], max_length=20)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('receiver_wallet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_transactions', to='transportation.wallet')),
                ('sender_wallet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_transactions', to='transportation.wallet')),
            ],
        ),
    ]
