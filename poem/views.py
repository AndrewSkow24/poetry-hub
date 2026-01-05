from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Poem


class PoemCreateView(CreateView):
    queryset = Poem.objects.all()
    fields = ["title", "content", "history"]
    template_name = "poem/poem_form.html"
    success_url = "/"


class PoemListView(ListView):
    queryset = Poem.objects.all()


class PoemDetailView(DetailView):
    queryset = Poem.objects.all()


class PoemUpdateView(UpdateView):
    queryset = Poem.objects.all()
    fields = ["title", "content", "history"]


class PoemDeleteView(DeleteView):
    queryset = Poem.objects.all()
    success_url = "/"
