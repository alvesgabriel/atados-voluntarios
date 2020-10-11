from django.urls import include, path
from rest_framework import routers
from voluntarios.voluntario import views

router = routers.DefaultRouter()
router.register(
    r"voluntarios",
    views.VoluntarioViewSet,
    basename="voluntarios",
)

urlpatterns = [
    path("", include(router.urls)),
]
