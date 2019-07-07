from rest_framework.routers import SimpleRouter
from .views import sampleView

router = SimpleRouter()
router.register(r'samples',sampleView)
urlpatterns = router.urls