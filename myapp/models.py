from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    patronymic = models.CharField(verbose_name='Отчество', max_length=120)
    phone = models.CharField(verbose_name='Телефон', max_length=12)

    def __str__(self):
        return self.username


class Orders(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('CustomUser', verbose_name='Автор', related_name='orders_customuser',
                              on_delete=models.CASCADE)
    status = models.ForeignKey('Status', verbose_name='Статуст', related_name='orders_status', on_delete=models.CASCADE)
    service = models.ForeignKey('TypeOfService', verbose_name='Тип услуги', related_name='orders_typeofservice',
                                on_delete=models.CASCADE)
    payment = models.ForeignKey('PaymentType', verbose_name='Тип платежа', related_name='orders_paymenttype',
                                on_delete=models.CASCADE)
    adress = models.CharField(verbose_name='Адрес', max_length=60)
    contact_phone = models.CharField(verbose_name='Телефон', max_length=12)
    # orderdate = models.DateField(blank=True, null=True)
    # ordertime = models.TimeField(blank=True, null=True)
    orderdatetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.created)

    class Meta:
        ordering = ['created']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Status(models.Model):
    title = models.CharField(verbose_name='Статус', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class TypeOfService(models.Model):
    title = models.CharField(verbose_name='Название', max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуг'


class PaymentType(models.Model):
    title = models.CharField(verbose_name='Тип платежа', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тип платежа'
        verbose_name_plural = 'Тип платежа'
