import django_filters
from projects.models import ProjectsModel

class ProjectsFilter(django_filters.FilterSet):
    name_project = django_filters.CharFilter(lookup_expr='icontains')
    created_from = django_filters.DateFilter(field_name='date_of_creation', lookup_expr='gte')
    created_to = django_filters.DateFilter(field_name='date_of_creation', lookup_expr='lte')
    sort_by = django_filters.OrderingFilter(
        fields=(
            ('name_project', 'name_project'),
            ('date_of_creation', 'date_of_creation'),
        ),
        field_labels={
            'name_project': 'Название проекта (от А до Я)',
            '-name_project': 'Название проекта (от Я до А)',
            'date_of_creation': 'Дата создания (от старых к новым)',
            '-date_of_creation': 'Дата создания (от новых к старым)',
        }
    )

    class Meta:
        model = ProjectsModel
        fields = ['name_project', 'created_from', 'created_to']