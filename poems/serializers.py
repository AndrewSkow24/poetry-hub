from rest_framework import serializers

from .models import Poem


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Poem
