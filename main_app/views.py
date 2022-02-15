from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from main_app.serializer import BookSerializer,ReporterSerializer,CompanySerializer,TicketSerializer
from main_app.models import Book,Reporter,Company,Ticket

class BookModelViewSet(ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny,]
    
class ReporterModelViewSet(ModelViewSet):
    
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer
    permission_classes = [AllowAny,]
    
class CompanyModelViewSet(ModelViewSet):
    
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny,]
    
class TicketModelViewSet(ModelViewSet):
    
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny,]
    
    