import django_filters

from .models import *

class studentFilter(django_filters.FilterSet):
    class Meta:
        model=student
        fields=['roll_no','name']