from django.shortcuts import render
from .models import Board, Section, Question, Answer, Mp3File, Player, Prize, Event

def home(request):
    file = Mp3File.objects.all()
    context = {
        'file': file
    }
    return render(request, 'home/home.html', context)

# Board

def board_menu(request):
    boards = Board.objects.all()
    return render(request, 'board/board_menu.html', {'boards': boards})

def board(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board': board
    }
    return render(request, 'board/board.html', context)

# Quiz

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

# List

def board_list(request):
    boards = Board.objects.all()
    return render(request, 'list/board_list.html', {'boards': boards})

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'list/section_list.html', {'sections': sections})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'list/question_list.html', {'questions': questions})

def answer_list(request):
    answers = Answer.objects.all()
    return render(request, 'list/answer_list.html', {'answers': answers})

def mp3file_list(request):
    mp3files = Mp3File.objects.all()
    return render(request, 'list/mp3file_list.html', {'mp3files': mp3files})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'list/player_list.html', {'players': players})

def prize_list(request):
    prizes = Prize.objects.all()
    return render(request, 'list/prize_list.html', {'prizes': prizes})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'list/event_list.html', {'events': events})
