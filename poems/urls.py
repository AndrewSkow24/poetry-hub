from .apps import PoemsConfig

app_name = PoemsConfig.name

from rest_framework.routers import DefaultRouter

from poems.views import PoemViewSet

router = DefaultRouter()

router.register("poem", PoemViewSet)

urlpatterns = [] + router.urls
