from django.urls import path,include
from project import views
urlpatterns = [
    path('', views.home),
    path('single_record/', views.single_record),
    path('files/', views.files),
    path('result/',views.result)
]
