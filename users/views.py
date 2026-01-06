from django.views.generic import DetailView, CreateView, ListView, UpdateView
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.urls import reverse_lazy


class ProfileListView(ListView):
    queryset = UserProfile.objects.all()
    template_name = "registration/profiles_list.html"


class ProfileDetailView(DetailView):
    queryset = UserProfile.objects.all()
    template_name = "registration/profile_detail.html"


class ProfileUpdateView(UpdateView):
    queryset = UserProfile.objects.all()
    template_name = "registration/profile_form.html"
    fields = "__all__"


class RegistrationUserView(CreateView):
    queryset = User.objects.all()
    form_class = RegistrationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("poem_list")
