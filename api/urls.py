from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='home'),
    path('create/', views.add_contact, name='add-items'),
    path('all/', views.view_contacts, name='view_items'),
    path('update/<int:pk>/', views.update_contacts, name='update-items'),
    path('item/<int:pk>/delete/', views.delete_contacts, name='delete-items'),
]
