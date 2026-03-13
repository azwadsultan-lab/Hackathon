from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('subject/', views.subject_detail_view, name='subject_detail'),
    path('verify/', views.verify_view, name='verify'),
    path('ask/', views.ask_view, name='ask'),
    path('profile/', views.profile_view, name='profile'),
]