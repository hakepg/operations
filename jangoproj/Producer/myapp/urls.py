from .views import *

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('place',PlaceOp)
router.register('restaurant',RestaurantOp)
router.register('waiter',WaiterOp)
router.register('customer',CustomerOp)

urlpatterns = router.urls