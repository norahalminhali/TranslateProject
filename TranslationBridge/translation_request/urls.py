from django.urls import path
from . import views

app_name = "translation_request"

urlpatterns = [
    path("create/", views.request_create_view, name="request_create_view"),
    path("list/", views.request_list_view, name="request_list_view"),
    path('detail/<int:pk>/', views.request_detail_view, name='request_detail_view'),
    path('update/<int:pk>/', views.request_update_view, name='request_update_view'),
]