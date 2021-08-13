import json
import requests
from statistic.clickhouse_models import Statistic
# from statistic.models import Statistic

def send_request(user_id):
    try:
        data = requests.get(url=f"http://127.0.0.1:8000/api/v1/accounts/{user_id}")
        print(data.status_code)
        if data.status_code == 200:
            account_data = data.json()
            if account_data['balance'] >= 1000:
                print(f"Account name {account_data['name']} - Balance {account_data['balance']}!")
            elif account_data['balance'] == 0:
                print(f"Account name {account_data['name']} - Zero balance!")
    except:
        pass


def get_balance():
    url ="http://127.0.0.1:8000/api/v1/accounts/balances/"
    data = requests.get(url)
    if data.status_code == 200:  
        result = data.json()
        balances = result['balance_sum']
        Statistic.objects.create(balance=balances)
        
        if balances > 100000:
            print(f"Sum of balances more than 100000. Balances = {balances}")
        return data.status_code

