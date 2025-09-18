from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', UserView)
router.register(r'assets', AssetView)
router.register(r'status', StatusView)
router.register(r'requests', RequestView)
router.register(r'photo', PhotoView)

urlpatterns = router.urls