from rest_framework import serializers

from main_app.models import Book, Reporter, Company, Ticket


class BookSerializer(serializers.ModelSerializer):
    id_copy = serializers.IntegerField(source='id')

    class Meta:
        model = Book
        exclude = []


class ReporterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reporter
        exclude = []


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        exclude = []


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        exclude = []
