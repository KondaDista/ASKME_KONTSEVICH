import copy
from tkinter.messagebox import QUESTION

from django.core.paginator import Paginator
from django.shortcuts import render

QUESTIONS = [
    {
        'title': f'Help Title-{i}',
        'id': i,
        'text': f'Some text for question number-{i}'
    }
    for i in range(1, 25)
]

ANSWERS = [
    {
        'id': i,
        'text': f'Some quick example text to build on the card title and make up the bulk of the cards content. Some quick example text to build on the card title and make up the bulk of the cards content. Number-{i}'
    }
    for i in range(1, 42)
]


def index(request):
    pageNum = int(request.GET.get('page', 1))
    page = paginate(pageNum, QUESTIONS)
    return render(
        request, 'index.html',
        context={'questions': page.object_list, 'page_obj': page})


def hotQuestion(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    return render(
        request, 'hot.html',
        context={'questions': hot_questions})


def question(request, question_id):
    currentQuestion = QUESTIONS[question_id - 1]
    pageNum = int(request.GET.get('page', 1))
    page = paginate(pageNum, ANSWERS, 4)
    return render(
        request, 'question.html',
        context={'questionItem': currentQuestion,'answers': page.object_list,  'page_obj': page})


def newQuestion(request):
    return render(request, 'newQuestion.html')


def tagQuestion(request, tag_name):
    return render(
        request, 'searchQuestion.html',
        context={'tag': tag_name})


def logIn(request):
    return render(request, 'logIn.html')


def registration(request):
    return render(request, 'registration.html')


def userProfile(request, user_name):
    return render(
        request, 'userProfile.html',
        context={'userName': user_name})


def paginate(objects_list, request, per_page=5):
    paginator = Paginator(request, per_page)
    page = paginator.page(objects_list)
    return page
