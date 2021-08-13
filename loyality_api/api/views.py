from django.db.models import Sum

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from account.models import Account
from api.serializers import AccountSerializer, ActionSerializer


class AccountCreateView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

class AccountDetailView(APIView):
    def get(self, request, pk):
        account = Account.objects.get(pk=pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)


class AccountAllBalancesView(APIView):
    def get(self, request):
        account = Account.objects.all()
        # serializer = AccountSerializer(account)
        balance_sum = account.aggregate(Sum('balance'))['balance__sum']
        result = {'balance_sum': balance_sum if balance_sum else 0}
        return Response(result)


class ActionCreateView(APIView):
    # {
    # "account": 9,
    # "action": "deposit",
    # "amount": 30000,
    # "description" : "another test deposit"
    # }
    def post(self, request):
        serializer = ActionSerializer(data=request.data)
        if serializer.is_valid():
            account = Account.objects.get(id=serializer.validated_data['account'].id)
            if serializer.validated_data['action'] == 'deposit':
                account.balance += serializer.validated_data['amount']
                account.save()
            elif serializer.validated_data['action'] == 'withdrawal':
                if account.balance - serializer.validated_data['amount'] >= 0:
                    account.balance -= serializer.validated_data['amount']
                    account.save()
                else:
                    return Response(data="Нельзя списать больше чем есть", status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            try:
                rq = requests.get(url="http://127.0.0.1:8001/statistic/user_id", params={"user_id":account.id})
            finally:
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
