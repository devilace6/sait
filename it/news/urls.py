from django.urls import path
from . import views
import include

urlpatterns = [
    path('', views.news_home, name ='news_home'),
    path("search/", views.Search.as_view(), name="search"),
    path('create', views.create, name='create'),
    path('filter/', views.FilterCatalogView, name="filter"),
    path('<slug:slug>', views.NewsDetail.as_view(), name='news_detail'),
    path('<slug:slug>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<slug:slug>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    path('<slug:category_slug>/', views.news_home, name = 'catalog_home_by_category'),
]