from django.urls import path
from .views import MainListView, ItemCreateView,ItemDeleteView,ItemUpdateView, LayoutCreateView,LayoutDeleteView
from . import views as main_views

urlpatterns = [
    path('', MainListView.as_view(), name='main-home'),
    # path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/', ItemUpdateView.as_view(), name='item-detail'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('layout/new/', LayoutCreateView.as_view(), name='layout-create'),
    path('layout/<int:pk>/delete/', LayoutDeleteView.as_view(), name='layout-delete')


]