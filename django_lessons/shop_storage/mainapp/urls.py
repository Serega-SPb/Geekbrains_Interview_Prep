from rest_framework.routers import DefaultRouter

from .views import StorageItemView

app_name = 'mainapp'

router = DefaultRouter()
router.register(r'items', StorageItemView, basename='user')
urlpatterns = router.urls
