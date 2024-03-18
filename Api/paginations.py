from rest_framework.pagination import PageNumberPagination



class PageNUmberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'

