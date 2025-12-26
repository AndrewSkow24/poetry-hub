from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Poem


class PoemSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        fields = "__all__"
        model = Poem
