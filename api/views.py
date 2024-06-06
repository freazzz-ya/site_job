from rest_framework import generics

from job.models import Earning_scheme, Expenses_model, Neural_network
from users.models import Worker

from .serializers import (EarningSchemeSerializer, ExpensesSerializer,
                          NetworkSerializers, UsersSerializers)


class UsersApiView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = UsersSerializers


class NeuronetApiView(generics.ListAPIView):
    queryset = Neural_network.objects.all()
    serializer_class = NetworkSerializers


class EarningSchemeApiView(generics.ListAPIView):
    queryset = Earning_scheme.objects.all()
    serializer_class = EarningSchemeSerializer


class ExpensesApiView(generics.ListAPIView):
    queryset = Expenses_model.objects.all()
    serializer_class = ExpensesSerializer
