# eduai/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views  # Importig the views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Connection of the empty URL to  home_view
]