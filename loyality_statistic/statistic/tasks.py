from core.celery import app
from statistic.services import get_balance, send_request


@app.task
def check_balance_by_id(user_id):
    send_request(user_id)



@app.task
def check_balance_sum():
    get_balance()