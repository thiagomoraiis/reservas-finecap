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
from django.core.paginator import Paginator

class IndexListView(ListView):
    model = Reserva
    template_name = 'reservas/pages/index.html'
    queryset = Reserva.objects.all().order_by('date')
    context_object_name = 'reservas'

    def get_queryset(self):
        qs = super().get_queryset()
        reservas = Reserva.objects.all()

        searched_name = self.request.GET.get('search-name')
        searched_value = self.request.GET.get('search-value')
        searched_payed = self.request.GET.get('search-payed')
        searched_date = self.request.GET.get('search-date')

        if searched_name:
            reservas = reservas.filter(nome_empresa__icontains=searched_name)

        if searched_value:
            reservas = reservas.filter(stand__valor=searched_value)

        if searched_payed is not None:
            reservas = reservas.filter(quitado=str(searched_payed))

        if searched_date:
            reservas = reservas.filter(date__gte=searched_date)

        paginator = Paginator(reservas, 2)
        pagina = self.request.GET.get("pagina")
        pag_obj = paginator.get_page(pagina)

        return pag_obj


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
