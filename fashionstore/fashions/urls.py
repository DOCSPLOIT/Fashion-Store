from rest_framework import routers
from .api import FashionViewset

router = routers.DefaultRouter()
router.register('api/fashions', FashionViewset, 'fashions')

urlpatterns = router.urls
