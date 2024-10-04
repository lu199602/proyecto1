from rest_framework.routers import DefaultRouter
from proyecto1.apis.views import productosViewSet

router = DefaultRouter()
router.register('productos', productosViewSet, basename='Productoo')
urlpatterns = router.urls