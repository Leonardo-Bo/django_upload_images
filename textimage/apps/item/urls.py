from django.urls import path
from .views import (HomeView, CreateItemView, UpdateItemView, 
                    DetailItemView, DeleteItemView, DeleteImageView, 
                    ItemValidationView)
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('create-item/', CreateItemView.as_view(), name='create_item'),
    path('edit-item/<int:pk>', UpdateItemView.as_view(), name='edit_item'), 
    path('detail-item/<int:pk>', DetailItemView.as_view(), name='detail_item'), 
    path('delete-item/<int:pk>', DeleteItemView.as_view(), name='delete_item'), 
    path('edit-item/<int:pk>/', DeleteImageView.as_view(), name='delete_image'), 
    path('create-item/validate-title/', csrf_exempt(ItemValidationView.as_view()), name="validate-title"),
]
