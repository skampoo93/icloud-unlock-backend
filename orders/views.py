from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderCreateSerializer, OrderAdminSerializer


class OrderCreateView(generics.CreateAPIView):
    """Le client connecté passe une commande (device_type + serial_number)."""
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class MyOrdersView(generics.ListAPIView):
    """Le client voit l'historique de SES propres commandes."""
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class AdminOrderListView(generics.ListAPIView):
    """
    L'ADMIN voit TOUTES les commandes de TOUS les utilisateurs,
    avec le numéro de série saisi par chacun.
    """
    queryset = Order.objects.all()
    serializer_class = OrderAdminSerializer
    permission_classes = [permissions.IsAdminUser]


class AdminOrderDetailView(generics.RetrieveUpdateAPIView):
    """L'ADMIN peut consulter/mettre à jour le statut d'une commande précise."""
    queryset = Order.objects.all()
    serializer_class = OrderAdminSerializer
    permission_classes = [permissions.IsAdminUser]
