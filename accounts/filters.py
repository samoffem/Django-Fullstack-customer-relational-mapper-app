from django_filters import FilterSet, DateFilter,CharFilter
from .models import Order


class OrderFilter(FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['date_created', 'customer']