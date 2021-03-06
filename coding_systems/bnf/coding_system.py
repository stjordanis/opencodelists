from functools import reduce

from django.db.models import Q

name = "Pseudo BNF"
short_name = "BNF"


def code_to_description_map(codes):
    from .models import Presentation

    presentations = Presentation.objects.filter(code__in=codes)
    return {p.code: p.name for p in presentations}


def codes_from_query(query):
    from .models import Presentation

    prefixes = query.splitlines()
    clauses = [Q(code__startswith=prefix) for prefix in prefixes]
    filter_arg = reduce(Q.__or__, clauses[1:], clauses[0])
    return list(Presentation.objects.filter(filter_arg).values_list("code", flat=True))
