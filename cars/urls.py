from django.urls import path
from . import views
urlpatterns = [
    path('details/<int:id>/', views.CarDetailView.as_view(), name='car_details'),
    path('buy/<int:id>/', views.CarBuy.as_view(), name='car_buy')
]
