from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('about/', views.about, name='about'),
    path('bills/', views.bills_index, name='index'),
    # path('bills/<int:bill>/', views.cats_detail, name='detail'),
    # path('bills/create/', views.CatCreate.as_view(), name='cats_create'),
    # path('bills/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    # path('bills/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),

]