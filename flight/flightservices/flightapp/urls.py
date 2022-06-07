from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# rounters are for viewset.
router = DefaultRouter()
router.register('flights', views.FlightViewSet)
router.register('passenger', views.PassengerViewSet)
router.register('reservation', views.ReservationViewSet)

urlpatterns = [
    path('flightServices/', include(router.urls)),
    path('flightServices/findflights', views.find_flights),
    path('flightServices/saveReservation', views.save_reservation),
]