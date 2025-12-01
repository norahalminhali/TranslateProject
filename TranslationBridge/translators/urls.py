from django.urls import path
from . import views

app_name = "translators"

urlpatterns = [
    path("create-new/", views.create_translator_view, name= "create_translator_view"),
]