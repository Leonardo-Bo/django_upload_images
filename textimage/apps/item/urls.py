from django.urls import path
from .views import HomeView, CreateItemView, UpdateItemView, DetailItemView, DeleteItemView, DeleteImageView

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('create-item/', CreateItemView.as_view(), name='create_item'),
    path('edit-item/<int:pk>', UpdateItemView.as_view(), name='edit_item'), 
    path('detail-item/<int:pk>', DetailItemView.as_view(), name='detail_item'), 
    path('delete-item/<int:pk>', DeleteItemView.as_view(), name='delete_item'), 
    path('edit-blogpost/<int:pk>/', DeleteImageView.as_view(), name='delete_image'), 
]
