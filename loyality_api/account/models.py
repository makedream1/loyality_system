from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='User', blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name='Username')
    balance = models.IntegerField(default=0, verbose_name='Balance')

    class Meta:
        db_table = 'account'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return f'{self.name}'


class Action(models.Model):
    ACTION_CHOICES = (
        ('deposit', 'deposit'),
        ('withdrawal', 'withdrawal')
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, verbose_name='Account')
    action = models.CharField(max_length=15, choices=ACTION_CHOICES, verbose_name='Action')
    amount = models.PositiveIntegerField(verbose_name='Amount')
    description = models.CharField(
        max_length=255, blank=True, verbose_name='Description')
    action_date = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='Action Date')

    class Meta:
        db_table = 'account_actions'
        verbose_name = 'Action'
        verbose_name_plural = 'Actions'

    def __str__(self):
        return f'{self.account.name}: {self.amount} {self.action}'
