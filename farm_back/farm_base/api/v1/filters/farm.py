from django_filters import FilterSet, filters

from farm_base.api.v1.filters.fields import NumberInFilter, CharInFilter
from farm_base.models import Farm


class FarmFilter(FilterSet):
  municipalities = CharInFilter(field_name='municipality', lookup_expr='in')
  states = CharInFilter(field_name='state', lookup_expr='in')

  class Meta:
      model = Farm
      fields = ['id', 'name', 'municipalities', 'states', 'owner__name', 'owner__document']