from django.db.models import Count
from django.core.paginator import Paginator
from django.shortcuts import render
from application.models import Question, Answer


def index(request):
    questions = Question.objects.all().annotate(num_answers = Count('answer'))
    page = paginate(questions)
    return render(
        request, 'index.html',
        context={'questions': page.object_list, 'page_obj': page})


def hotQuestion(request):
    hot_questions = Question.objects.get_hot_question()
    page = paginate(hot_questions)
    return render(
        request, 'hot.html',
        context={'questions': page.object_list, 'page_obj': page})


def question(request, question_id):
    currentQuestion = Question.objects.filter(id__exact = question_id).first()
    answers = Answer.objects.get_answer_by_question(question_id)
    page = paginate(answers, 4)
    return render(
        request, 'question.html',
        context={'questionItem': currentQuestion, 'answers': page.object_list,  'page_obj': page})


def ask(request):
    return render(request, 'ask.html')


def tagQuestion(request, tag_name):
    questions = Question.objects.filter(tags__name__exact = tag_name)
    return render(
        request, 'searchByTagQuestion.html',
        context={'questions': questions, 'tag': tag_name})


def logIn(request):
    return render(request, 'logIn.html')


def registration(request):
    return render(request, 'registration.html')


def userProfile(request, user_name):
    return render(
        request, 'userProfile.html',
        context={'userName': user_name})


def paginate(request, per_page=5):
    # pageNum = int(request.GET.get('page', 1))
    paginator = Paginator(request, per_page)
    page = paginator.page(1)
    return page

