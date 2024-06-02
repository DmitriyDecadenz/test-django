from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TransactionListSerializer, TransactionDetailSerializer, TransactionCreateSerializer
from .models import Transaction
from rest_framework import generics
from rest_framework.permissions import AllowAny


class TransactionListView(generics.ListAPIView):
    """Вывод всех транзакций"""
    serializer_class = TransactionListSerializer
    permission_classes = [AllowAny]
    queryset = Transaction.objects.all()


class TransactionDetailView(generics.RetrieveAPIView):
    """Вывод транзакций по айди транзакции"""
    serializer_class = TransactionDetailSerializer
    permission_classes = [AllowAny]
    queryset = Transaction.objects.all()


class TransactionDetailUserView(generics.ListAPIView):
    """Вывод транзакций по айди пользователя"""
    serializer_class = TransactionDetailSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def get_queryset(self):

        queryset = Transaction.objects.all()
        user_id = self.request.query_params.get('user')
        if user_id is not None:
            queryset = Transaction.objects.filter(user=user_id)
        return queryset


class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionCreateSerializer
