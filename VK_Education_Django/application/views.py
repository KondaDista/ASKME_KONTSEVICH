from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from application.models import Question, Answer


def index(request):
    questions = Question.objects.get_all_questions()
    page = paginate(request, questions)
    return render(
        request, 'index.html',
        context={'questions': page.object_list, 'page_obj': page})


def hotQuestion(request):
    hot_questions = Question.objects.get_hot_questions()
    page = paginate(request, hot_questions)
    return render(
        request, 'hot.html',
        context={'questions': page.object_list, 'page_obj': page})


def question(request, question_id):
    currentQuestion = Question.objects.get_question(question_id)
    answers = Answer.objects.get_answer_by_question(question_id)
    page = paginate(request, answers, 4)
    return render(
        request, 'question.html',
        context={'questionItem': currentQuestion, 'answers': page.object_list,  'page_obj': page})


def ask(request):
    return render(request, 'ask.html')


def tagQuestion(request, tag_name):
    questions = Question.objects.get_questions_by_tag(tag_name)
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


def paginate(request, query_list, per_page=5):
    pageNum = request.GET.get('page', 1)
    print(pageNum)
    paginator = Paginator(query_list, per_page)
    try:
        return paginator.get_page(pageNum)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

