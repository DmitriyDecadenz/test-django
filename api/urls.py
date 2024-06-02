from django.urls import path
from api.views import (TransactionListView,
                       TransactionDetailView,
                       TransactionCreateView, TransactionDetailUserView)
from api.spectacular.urls import urlpatterns as doc_urls

app_name = 'api'

urlpatterns = [
    path('transactions/', TransactionListView.as_view()),
    path('transaction/<int:pk>/', TransactionDetailView.as_view()),
    path('user/transactions/', TransactionDetailUserView.as_view()),
    path('transactions/new/', TransactionCreateView.as_view()),
]

urlpatterns += doc_urls
