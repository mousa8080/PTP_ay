from django.db import models

class User(models.Model):
    USER_TYPES = (
        ('passenger', 'Passenger'),
        ('driver', 'Driver'),
        ('admin', 'Admin'),
    )
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user}"

class Vehicle(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'driver'})
    license_plate = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    gps_enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.driver}"
class Route(models.Model):
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    total_distance = models.DecimalField(max_digits=6, decimal_places=2)
    estimated_time = models.DurationField()
    def __str__(self):
        return self.start_point

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('fare_payment', 'Fare Payment'),
        ('wallet_topup', 'Wallet Top-up'),
        ('transfer', 'Transfer'),
    )
    STATUS_TYPES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    sender_wallet = models.ForeignKey(Wallet, related_name='sent_transactions', on_delete=models.CASCADE, null=True, blank=True)
    receiver_wallet = models.ForeignKey(Wallet, related_name='received_transactions', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    status = models.CharField(max_length=10, choices=STATUS_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.transaction_type} from {self.sender_wallet} to {self.receiver_wallet}"

class Ticket(models.Model):
    PAYMENT_METHODS = (
        ('NC', 'Non-Cash'),
        ('QR', 'QR Payment'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    fare = models.DecimalField(max_digits=5, decimal_places=2)
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHODS)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Ticket for {self.user} on {self.vehicle}"
  
class Report(models.Model):
    STATUS_TYPES = (
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('resolved', 'Resolved'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reports')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver_reports')
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Report for {self.user} by {self.driver}"

class VehicleTracking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.vehicle} - Latitude: {self.latitude}, Longitude: {self.longitude}, Speed: {self.speed}"


class DriverEarnings(models.Model):
    STATUS_TYPES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    )
    driver = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'driver'})
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_TYPES)
    confirmed_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.driver} - Amount: {self.amount}, Status: {self.status}"
