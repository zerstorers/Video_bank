from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ClientInlineFormSet
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView
from .models import Client


# Create your views here.

class ClientListView(ListView):
    model=Client

class ClientDetailView(DetailView):
    model=Client

class DeleteClientView(DeleteView):
    model=Client
    slug_field = "id"
    success_url = reverse_lazy('home')


class CreateClientView(CreateView):
    fields = "__all__"
    model = Client

    permission_required = ("Client.add_client")

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['Client_form'] = ClientInlineFormSet()
        return context

    def form_valid(self, form):
        if form.is_valid():
            self.new_Client = form.save(commit=False)

            Client_form = ClientInlineFormSet(self.request.POST, instance=self.new_Client)

            if Client_form.is_valid():
                form.save()
                Client_form.save()
                return HttpResponseRedirect(self.get_success_url())
            context = {
                'form': form,
                'Client_form': Client_form,
                }
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy("detail_Clients", args=[self.new_Client.id])

