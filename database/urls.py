from django.urls import path
from database import views

urlpatterns = [
    path('', views.home, name='home'),
    path('board/', views.board_menu, name='board_menu'),
    path('board/<int:pk>/', views.board, name='board'),
    path('quiz/', views.quiz_menu, name='quiz_menu'),
    path('quiz/<int:pk>/', views.quiz, name='quiz'),
    path('list/boards/', views.board_list, name='board_list'),
    path('list/sections/', views.section_list, name='section_list'),
    path('list/questions/', views.question_list, name='question_list'),
    path('list/answers/', views.answer_list, name='answer_list'),
    path('list/mp3files/', views.mp3file_list, name='mp3file_list'),
    path('list/players/', views.player_list, name='player_list'),
    path('list/prizes/', views.prize_list, name='prize_list'),
    path('list/events/', views.event_list, name='event_list'),
]
