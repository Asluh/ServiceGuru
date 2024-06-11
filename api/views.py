from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from rest_framework import authentication,permissions

from api.serializers import CustomerSerializers

from api.models import Customer


class CustomerViewsetView(ModelViewSet):

    serializer_class=CustomerSerializers

    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):
        
        serializer.save(technician=self.request.user)
