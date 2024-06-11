from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter

from api import views

router=DefaultRouter()

router.register('customer',views.CustomerViewsetView,basename='customer')

urlpatterns=[
    path('token/',ObtainAuthToken.as_view(),name='obtaintoken'),
]+router.urls