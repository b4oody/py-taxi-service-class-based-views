from django.urls import path

from .views import (
    index,
    ManufacturerListView,
    CarListView,
    CarDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>", CarDetailView.as_view(), name="car-detail"),
]

app_name = "taxi"
