from django.contrib import admin
from .models import Contact,myPersonalInfo,portfolio
# Register your models here.
admin.site.register(Contact)
admin.site.register(myPersonalInfo)
admin.site.register(portfolio)