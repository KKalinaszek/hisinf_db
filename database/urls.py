from django.urls import path
from database import views

urlpatterns = [
    path('', views.home, name='home'),
    path('board/', views.board_menu, name='board_menu'),
    path('board/<int:pk>/', views.board, name='board'),
    path('quiz/', views.quiz_menu, name='quiz_menu'),
    path('quiz/<int:pk>/', views.quiz, name='quiz'),
]
