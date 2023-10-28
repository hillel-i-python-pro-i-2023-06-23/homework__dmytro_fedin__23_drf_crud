from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='home'),
    path('create/', views.add_contact, name='add-contacts'),
    path('all/', views.view_contacts, name='view_contacts'),
    path('update/<int:pk>/', views.update_contacts, name='update-contacts'),
    path('contact/<int:pk>/delete/', views.delete_contacts, name='delete-contacts'),
]
