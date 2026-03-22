"""
URL configuration for flightServices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from trainApp import views
from rest_framework.routers import DefaultRouter

# Create router to automatically handle CRUD APIs for ViewSets
router = DefaultRouter()

# Register each ViewSet with a URL
router.register('trains', views.TrainViewSet)
router.register('passengers', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)

urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),

    # All ViewSet APIs will be available under /trainServices/
    # Example: /trainServices/trains/, /trainServices/reservations/
    path('trainServices/', include(router.urls)),

    # Custom API to find trains based on source, destination, and date
    path('trainServices/find_trains/', views.find_trains),
]
