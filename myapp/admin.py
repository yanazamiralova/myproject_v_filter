from django.contrib import admin
from .models import Status, Orders, PaymentType, TypeOfService, CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'patronymic', 'email', 'phone', 'is_staff')
    list_display_links = ('id', 'username', 'first_name', 'last_name', 'patronymic', 'email', 'phone', 'is_staff')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'status', 'service', 'payment', 'adress', 'orderdatetime')
    list_display_links = ('id', 'owner', 'status', 'service', 'payment', 'adress', 'orderdatetime')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(TypeOfService)
class TypeOfServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
