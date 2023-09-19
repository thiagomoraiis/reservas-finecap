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
    queryset = Reserva.objects.all().order_by('date')
    context_object_name = 'reservas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request == 'GET':
            searched_name = self.request.GET['search-name']
            searched_value = self.request.GET['search-value']
            searched_payed = self.request.GET['search-payed']
            searched_date = self.request.GET['search-date']
            reservas = Reserva.objects.filter(nome_empresa__contains=searched_name, stand__valor=searched_value, quitado=searched_payed, date=searched_date)
            context['reservas'] = reservas
            return context
        else:
            pass
        return context


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
