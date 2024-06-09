from rest_framework import generics

from job.models import (
                        Earning_scheme, Expenses_model,
                        Neural_network, Job_Payment,
                        Other_Source, Network_Payment,)
from users.models import Worker

from .serializers import (EarningSchemeSerializer, ExpensesSerializer,
                          NetworkSerializers, UsersSerializers,
                          JobPaymentSerializer, NetworkPaymentSerializer,
                          OtherSourceSerializer)


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


class JobApiView(generics.ListAPIView):
    queryset = Job_Payment.objects.all()
    serializer_class = JobPaymentSerializer


class NetworkApiView(generics.ListAPIView):
    queryset = Network_Payment.objects.all()
    serializer_class = NetworkPaymentSerializer


class OtherSource(generics.ListAPIView):
    queryset = Other_Source.objects.all()
    serializer_class = OtherSourceSerializer
