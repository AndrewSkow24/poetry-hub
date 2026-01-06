from django.views.generic import DetailView
from .models import UserProfile


class ProfileDetailView(DetailView):
    queryset = UserProfile.objects.all()
