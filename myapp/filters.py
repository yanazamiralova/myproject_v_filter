import django_filters
from .models import Orders


class OrdersFilter(django_filters.FilterSet):
    orderdatetime = django_filters.DateFromToRangeFilter(field_name='orderdatetime', label='Диапазон дат выполнения')
    adress = django_filters.CharFilter(lookup_expr='icontains', label='Адрес')
    contact_phone = django_filters.CharFilter(lookup_expr='icontains', label='Телефон')

    class Meta:
        model = Orders
        fields = {
            'status',
            'contact_phone',
            'service',
            'payment',
            'orderdatetime',
            'adress',
        }
