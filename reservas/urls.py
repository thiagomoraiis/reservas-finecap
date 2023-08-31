from django.urls import path
from .views import (
    IndexListView,
    ReservaCreateView,
    ReservaDetailView,
    ReservaDeleteView,
    ReservaUpdateView
    )

urlpatterns = [
    path(
        '', IndexListView.as_view(), name='index'
    ),
    path(
        'create/', ReservaCreateView.as_view(), name='create-reserva'
    ),
    path(
        'detail/<int:id>/', ReservaDetailView.as_view(), name='detail-reserva',
    ),
    path(
        'delete/<int:id>/', ReservaDeleteView.as_view(), name='delete-reserva'
    ),
    path(
        'update/<int:id>/', ReservaUpdateView.as_view(), name='update-reserva'
    ),
]
