from django.urls import path
from statistic.views import notify_by_id

urlpatterns = [
    path('user_id', notify_by_id),
]