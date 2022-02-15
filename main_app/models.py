from django.db import models
from datetime import date

class Book(models.Model):
    
    word = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.author}, - {self.word}"

class Reporter(models.Model):

    name = models.CharField(max_length=255)
    stories_filed = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}, - {self.stories_filed}"


class Company(models.Model):
    
    num_employees = models.PositiveIntegerField()
    num_chairs = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.manufacturer}, - {self.num_employees}, {self.num_chairs}"
    
class Ticket(models.Model):
    
    duartion = models.DurationField()
    active_at = models.DateField(default=date.today)
    
    def __str__(self):
        return f"{self.duartion} - {self.active_at}"
