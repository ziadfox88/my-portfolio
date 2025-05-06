from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    # path('post/<int:year>/<int:month>/<int:day>/<slug:post>', views.portofolio, name='portofolio'),
]