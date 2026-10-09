from django.conf import settings
from django.db import models


class Order(models.Model):
    class DeviceType(models.TextChoices):
        IPHONE = "iphone", "Vérification iPhone"
        MACBOOK = "macbook", "Vérification MacBook"
        IPAD = "ipad", "Vérification iPad"

    class Status(models.TextChoices):
        PENDING = "pending", "En attente"
        IN_PROGRESS = "in_progress", "En cours de traitement"
        DONE = "done", "Terminée"
        REJECTED = "rejected", "Rejetée"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    device_type = models.CharField(max_length=20, choices=DeviceType.choices)
    serial_number = models.CharField(max_length=100)

    # Champ optionnel, désactivé par défaut côté frontend, mais prêt si vous
    # voulez exiger un justificatif de propriété (facture, etc.) plus tard.
    proof_of_ownership = models.FileField(
        upload_to="proofs/", blank=True, null=True
    )

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.IN_PROGRESS
    )
    admin_note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Commande #{self.id} - {self.user.username} - {self.device_type} - {self.serial_number}"
