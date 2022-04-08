from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('vehicls', views.vehiclsviewset)

urlpatterns =[
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework'))
]