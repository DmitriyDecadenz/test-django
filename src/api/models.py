from typing import Union

from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from src.config import settings


class Account(models.Model):
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT  # we cannot delete user with money
    )

    def __str__(self):
        return f'{self.id} of {self.user.username}'


class Action(models.Model):
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    date = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='actions',
    )

    def __str__(self):
        return f'Account number {self.account.id} ' +\
            f'was changed on {str(self.amount)}'


class Transaction(models.Model):

    class PaymentMethod(models.TextChoices):
        """Статус доставки."""
        CASH = 'CS', _('Наличными.')
        CART = 'CT', _('Картой.')
        ONLINE_WALLET = 'OW', _('Онлайн кошелек.')

    method = models.CharField(
        verbose_name='Метод оплаты',
        max_lenght=2,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CART
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    date = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'Account number {self.account.id} '

    @classmethod
    def make_transaction(cls, amount, account, merchant) -> Union[dict | tuple]:
        if account.balance < amount:
            raise(ValueError('Not enough money'))

        with transaction.atomic():
            account.balance -= amount
            account.save()
            tran = cls.objects.create(
                amount=amount, account=account)

        return account, tran


class Transfer(models.Model):

    from_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='from_account'
    )

    to_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='to_account'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
