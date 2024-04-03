from django.shortcuts import render

from django.http import HttpResponse, Http404
from .models import Board

def home(request):
    boards = Board.objects.all()
    # boards_names = []

    # for board in boards:
    #     boards_names.append(board.name)

    # response_html = '<br>'.join(boards_names)

    # return HttpResponse(response_html)
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board':board})
    # return HttpResponse("List of board topics")

def about(request):
    # do something...
    return render(request, 'about.html')

def question(request, pk):
    return HttpResponse(f"Question : {pk}")

def post(request, slug):
    return HttpResponse(f"slug : {slug}")

def blog_post(request, slug, pk):
    return HttpResponse(f"Blog_post : {slug} and PK : {pk}")

def user_profile(request, username):
    return HttpResponse(f"User Name : {username}")

def year_archive(request, year):
    return HttpResponse(f"Year : {year}")


    