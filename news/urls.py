from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contact/', views.contact_page, name='contact'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('category/create/', views.create_category, name='create_category'),
    path('category/<slug:slug>/', views.CategoryNewsView.as_view(), name='category'),
    path('create/', views.create_news, name='create_news'),
]
