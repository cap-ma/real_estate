from django.urls import path
from .views import ApartmentListView,ApartmentDetailView,BannerListView,UserFormCreateView,AparetmentUserFormCreateView

urlpatterns=[
    path('apartment-list',ApartmentListView.as_view(),name='apartment-list'),
    path('apartment-detail/<int:pk>',ApartmentDetailView.as_view(),name='apartment-detail'),
    path('banner-list',BannerListView.as_view(),name='banner-list'),
    path('user-form',UserFormCreateView.as_view(),name='user-form'),
    path('apartment-user-form',AparetmentUserFormCreateView.as_view(),name='apartment-form'),
]