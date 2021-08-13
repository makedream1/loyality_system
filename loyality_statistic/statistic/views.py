from django.http import HttpResponse
from statistic.tasks import check_balance_by_id

def notify_by_id(request):
    if request.GET:
        user = request.GET.get('user_id')
        check_balance_by_id.delay(user)
    return HttpResponse()