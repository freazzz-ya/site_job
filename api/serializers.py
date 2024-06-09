from rest_framework import serializers

from job.models import (Earning_scheme, Expenses_model, Job_Payment,
                        Network_Payment, Neural_network, Other_Source)
from users.models import Worker


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = [
            'id', 'username', 'first_name',
            'last_name', 'is_staff', 'email',
            'description_for_profil', 'image',
            'telegram_id',
        ]


class NetworkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Neural_network
        fields = [
            'title', 'image', 'description',
            'url', 'date_joined',
        ]


class EarningSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earning_scheme
        fields = [
            'worker', 'title', 'network',
            'other_source', 'image', 'url',
            'discription', 'date_joined',
        ]


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses_model
        fields = [
            'author', 'comment', 'type_expenses',
            'variety', 'price', 'date',
        ]


class JobPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Payment
        fields = [
            'worker', 'payment_in_money', 'date',
        ]


class OtherSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other_Source
        fields = [
            'worker', 'payment_in_money', 'date',
        ]


class NetworkPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network_Payment
        fields = [
            'worker', 'payment_in_money', 'date',
        ]
