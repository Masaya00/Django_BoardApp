from django.contrib import admin
from django.urls import path
from .views import PostFormView, CommentFormView


app_name = 'Board_App'
urlpatterns = [
    path('', PostFormView.as_view(), name='post_list'),
    path('post/<int:pk>', CommentFormView.as_view(), name='post_comment'),
]