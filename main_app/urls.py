from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter

from main_app.views import BookModelViewSet,ReporterModelViewSet,CompanyModelViewSet,TicketModelViewSet

router = SimpleRouter()
router.register('book',BookModelViewSet)
router.register('Reporter',ReporterModelViewSet)
router.register('Company',CompanyModelViewSet)
router.register('Ticket',TicketModelViewSet)

urlpatterns = []
urlpatterns += router.urls