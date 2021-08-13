from rest_framework import serializers

from account.models import Account, Action


class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ('user_id', 'name', 'balance',)


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        exclude = ('action_date',)