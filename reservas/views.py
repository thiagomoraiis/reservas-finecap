from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)
from django.contrib.auth.decorators import login_required

from .models import Reserva
from .forms import ReservaModelForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required(login_url='/user/login')
class IndexListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'reservas/pages/index.html'
    queryset = Reserva.objects.all()
    context_object_name = 'reservas'
    login_url = '/user/login/'

class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    form_class = ReservaModelForm
    template_name = 'reservas/pages/reserva_form.html'
    success_url = reverse_lazy('index')
    login_url = '/user/login/'

class ReservaDetailView(LoginRequiredMixin, DetailView):
    model = Reserva
    queryset = Reserva.objects.all()
    context_object_name = 'reserva'
    pk_url_kwarg = 'id'
    template_name = 'reservas/pages/reserva.html'
    login_url = '/user/login/'

class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reserva
    form_class = ReservaModelForm
    pk_url_kwarg = 'id'
    template_name = 'reservas/pages/reserva_form.html'
    login_url = '/user/login/'
    success_url = reverse_lazy('index')

class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    context_object_name = 'reserva'
    template_name = 'reservas/pages/confirmacao_exclusao.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index')
    login_url = '/user/login/'
