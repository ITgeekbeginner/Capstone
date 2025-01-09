from rest_framework.pagination import PageNumberPagination

class RecipePagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'  # Allow users to define the page size in the query parameters
    max_page_size = 100  
