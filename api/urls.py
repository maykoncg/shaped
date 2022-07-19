from rest_framework import routers
from .views import PacienteViewSet,ExameViewSet
router = routers.SimpleRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'exames', ExameViewSet)
urlpatterns = router.urls