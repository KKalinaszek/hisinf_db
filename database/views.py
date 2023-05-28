from django.shortcuts import render
from .models import Board, Mp3File, Question, Answer

def home(request):
    file = Mp3File.objects.all()
    context = {
        'file': file
    }
    return render(request, 'home/home.html', context)

def board_menu(request):
    boards = Board.objects.all()
    return render(request, 'board/board_menu.html', {'boards': boards})

def board(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board': board
    }
    return render(request, 'board/board.html', context)

def quiz_menu(request):
    boards = Board.objects.all()
    questions = Question.objects.all()
    context = {
        'boards': boards,
        'questions': questions
    }
    return render(request, 'quiz/quiz_menu.html', context)

def quiz(request, pk):
    board = Board.objects.get(pk=pk)
    questions = Question.objects.filter(board_id=board.id)
    context = {
        'board': board,
        'questions': questions
    }
    return render(request, 'quiz/quiz.html', context)