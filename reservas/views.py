from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)


from .models import Reserva
from .forms import ReservaModelForm
from django.urls import reverse_lazy


class IndexListView(ListView):
    model = Reserva
    template_name = 'reservas/pages/index.html'
    queryset = Reserva.objects.all()
    context_object_name = 'reservas'


class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaModelForm
    template_name = 'reservas/pages/reserva_form.html'
    success_url = reverse_lazy('index')


class ReservaDetailView(DetailView):
    model = Reserva
    queryset = Reserva.objects.all()
    context_object_name = 'reserva'
    pk_url_kwarg = 'id'
    template_name = 'reservas/pages/reserva.html'


class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = ReservaModelForm
    pk_url_kwarg = 'id'
    template_name = 'reservas/pages/reserva_form.html'
    success_url = reverse_lazy('index')


class ReservaDeleteView(DeleteView):
    model = Reserva
    context_object_name = 'reserva'
    template_name = 'reservas/pages/confirmacao_exclusao.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index')
