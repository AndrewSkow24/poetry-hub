from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
    )
    pseudonym = forms.CharField(
        required=False, max_length=150, label="Псевдоним (необязательно)"
    )
    bio = forms.CharField(required=False, label="О себе (необязательно)")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                pseudonym=self.cleaned_data.get("pseudonym", ""),
                bio=self.cleaned_data.get("bio", ""),
            )
        return user
