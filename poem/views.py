from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Poem


class PoemCreateView(LoginRequiredMixin, CreateView):
    queryset = Poem.objects.all()
    fields = ["title", "content", "history"]
    template_name = "poem/poem_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PoemListView(ListView):
    queryset = Poem.objects.all()


class PoemDetailView(LoginRequiredMixin, DetailView):
    queryset = Poem.objects.all()


class PoemUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Poem.objects.all()
    fields = ["title", "content", "history"]


class PoemDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Poem.objects.all()
    success_url = "/"
