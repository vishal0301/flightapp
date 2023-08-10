from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, PassengerViewSet, ReservationViewSet
from .views import find_flights, save_reservation
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('passengers',PassengerViewSet)
router.register('reservation', ReservationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api-token'),
    path('findflights/', find_flights),
    path("saveReservation/", save_reservation ),
]