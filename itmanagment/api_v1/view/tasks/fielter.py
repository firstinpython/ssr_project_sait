import django_filters
from tasks.models import TaskModel

class TaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status__name_status', lookup_expr='icontains')
    priority = django_filters.CharFilter(field_name='priority__name_priority', lookup_expr='icontains')
    executor = django_filters.CharFilter(field_name='executor__username', lookup_expr='icontains')
    created_from = django_filters.DateFilter(field_name='date_of_creation', lookup_expr='gte')
    created_to = django_filters.DateFilter(field_name='date_of_creation', lookup_expr='lte')
    updated_from = django_filters.DateFilter(field_name='date_of_update', lookup_expr='gte')
    updated_to = django_filters.DateFilter(field_name='date_of_update', lookup_expr='lte')
    deadline_from = django_filters.DateFilter(field_name='date_of_deadline', lookup_expr='gte')
    deadline_to = django_filters.DateFilter(field_name='date_of_deadline', lookup_expr='lte')
    sort_by = django_filters.OrderingFilter(
        fields=(
            ('name_task', 'name_task'),
            ('date_of_creation', 'date_of_creation'),
            ('date_of_update', 'date_of_update'),
        ),
        field_labels={
            'name_task': 'Название задачи (от А до Я)',
            '-name_task': 'Название задачи (от Я до А)',
            'date_of_creation': 'Дата создания (от старых к новым)',
            '-date_of_creation': 'Дата создания (от новых к старым)',
            'date_of_update': 'Дата обновления (от старых к новым)',
            '-date_of_update': 'Дата обновления (от новых к старым)',
        }
    )

    class Meta:
        model = TaskModel
        fields = ['status', 'priority', 'executor', 'created_from', 'created_to', 'updated_from', 'updated_to', 'deadline_from', 'deadline_to']