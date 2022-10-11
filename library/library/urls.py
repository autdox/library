from django.urls import path
from library.library import views

urlpatterns = [
    path('book/', views.book_list),
    path('book/<int:pk>/', views.book_detail),
    path('book/<int:fk>/comments', views.comment_list),
    path('comment/<int:pk>', views.comment_detail),
]