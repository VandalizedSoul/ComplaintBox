from demo.models import Complain
import django_filters

class ComplainFilter(django_filters.FilterSet):
    complain_uname = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Complain
        fields = ['complain_status', 'complain_uname','complain_priority' ]