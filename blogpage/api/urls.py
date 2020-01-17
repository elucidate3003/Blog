from django.urls import path
from blogpage.api.views import article_get_data, article_update_data_view, article_add_data_view,search_get_data,article_delete_view

urlpatterns = [
    path('<slug>', article_get_data, name="get_data"),
    path('update/<slug>', article_update_data_view, name="update_data"),
    path('add/', article_add_data_view, name="add_data"),
    path('delete/<slug>', article_delete_view, name="delete_data"),
    path('search/',search_get_data, name="search_api"),

]
