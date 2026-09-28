from rest_framework import serializers
from .models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    """Utilisé par le CLIENT pour passer une commande."""

    class Meta:
        model = Order
        fields = ("id", "device_type", "serial_number", "proof_of_ownership", "status", "created_at")
        read_only_fields = ("id", "status", "created_at")

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class OrderAdminSerializer(serializers.ModelSerializer):
    """Utilisé par l'ADMIN : voit tout, y compris qui a passé la commande."""

    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Order
        fields = (
            "id", "username", "email", "device_type", "serial_number",
            "proof_of_ownership", "status", "admin_note", "created_at", "updated_at",
        )
        read_only_fields = ("id", "username", "email", "serial_number", "device_type", "created_at", "updated_at")
