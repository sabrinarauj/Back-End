import django_filters as df
from django.db.models import Q
from .models import Autor

class AutoFilter(df.FilterSet):
    nome = df.CharFilter(method='filter_nome')
    nation = df.CharFilter(method='filter_nacionalidade', lookup_expr='iexact')

    def filter_nome(self, qs, name, value: str):
        if not value:
            return qs
        return qs.filter(Q(nome__icontains=value) | (Q(sobrenome__icontains=value)))
    
    def filter_nation(self, qs, name, value: str):
        if not value:
            return qs
        return qs.filter(Q(nation__icontains=value))
    
    class Meta:
        model = Autor
        fields = []