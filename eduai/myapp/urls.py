from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('subject/', views.subject_detail_view, name='subject_detail'),
    
    # ADD THIS NEW LINE:
    path('ask/', views.ask_view, name='ask'),
]