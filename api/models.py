from django.db import models
from django.utils.translation import gettext_lazy as _
from config.settings import AUTH_USER_MODEL


class Transaction(models.Model):

    class PaymentMethod(models.TextChoices):
        """Методы оплаты"""
        CASH = 'CASH', _('Наличными.')
        CART = 'CART', _('Картой.')
        ONLINE_WALLET = 'ONLINE_WALLET', _('Онлайн кошелек.')

    class Currency(models.TextChoices):
        """Валюты."""
        RUB = 'RUB', _('Рубли.')
        EURO = 'EUR', _('Еврою')
        USD = 'USD', _('Доллар')

    class Status(models.TextChoices):
        """Статусы транзакции"""
        success = 'Success', _('Успешно')
        declined = 'Declined', _('Отменено')

    method = models.CharField(
        verbose_name='Метод оплаты',
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CART
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    date = models.DateTimeField(
        verbose_name='Дата',
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.PROTECT  # we cannot delete user with money
    )

    currency = models.CharField(
        verbose_name='Валюта',
        max_length=255,
        choices=Currency.choices,
        default=Currency.RUB
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=255,
        choices=Status.choices,
        default=Status.success
    )
    objects = models.Manager()

    def __str__(self) -> str:
        return f'Транзакция пользователя {self.user}'


