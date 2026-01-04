from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Poem


class PoemListView(ListView):
    queryset = Poem.objects.all()
