from re import search
from django.db.models import Q
from goods.models import Developer
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import SearchHeadline

def q_search(query):
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    
    result =  Developer.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query, 
            start_sel='<span style="background-color: rgba(180, 57, 57,0.5);">',
            stop_sel="</span>"))
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query, 
            start_sel='<span style="background-color: rgba(180, 57, 57,0.5);">',
            stop_sel="</span>"))
    return result