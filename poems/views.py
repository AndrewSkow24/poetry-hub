from rest_framework.viewsets import ModelViewSet
from .models import Poem
from .serializers import PoemSerializer


class PoemViewSet(ModelViewSet):
    model = Poem
    serializer_class = PoemSerializer
    queryset = Poem.objects.all()
