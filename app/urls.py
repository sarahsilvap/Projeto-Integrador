from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView, AssetView, StatusView, RequestView


router = DefaultRouter()

router.register(r'users', UserView)
router.register(r'assets', AssetView)
router.register(r'status', StatusView)
router.register(r'requests', RequestView)

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

