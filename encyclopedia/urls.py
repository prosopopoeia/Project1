from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path("", views.index, name="index"),
    path("newpage/", views.newpage, name="newpage"),
    path("displaypage/", views.entrypage, name="displaypage"),
    path("wiki/<str:utitle>", views.entrypage, name="entrypage"),
]
