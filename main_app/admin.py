from django.contrib import admin


from main_app.models import Ticket,Company,Book,Reporter


admin.site.register(Ticket)
admin.site.register(Company)
admin.site.register(Book)
admin.site.register(Reporter)
