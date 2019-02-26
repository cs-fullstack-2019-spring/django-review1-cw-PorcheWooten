from django.urls import path

# import endpoints_app
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('page2/', views.page2, name='page_2'),
    path('page3/', views.page3, name='page_3'),
    path('page4/', views.page4, name='page_4'),
    path('page5/', views.page5, name='page_5'),


]