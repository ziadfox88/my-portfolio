from django.contrib import admin
from .models import Contact,myPersonalInfo,portfolio
# Register your models here.

admin.site.register(Contact)


class MyPersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'hits')  # Display hit count in list view
    readonly_fields = ('hits',)  # Prevent manual edits of hit count

admin.site.register(myPersonalInfo, MyPersonalInfoAdmin)


@admin.register(portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish')
    # prepopulated_fields = {'slug':('title', )}
    # date_hierarchy = 'publish'
    # ordering = ['status','publish']


