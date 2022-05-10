from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from rest_framework_swagger.views import get_swagger_view




def login(request):
    return redirect('login')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# @login_required
def index(request):
    courses = Course.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'courses': courses})


@login_required
def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('sections')

        # if form.is_valid():
        #     section = form.save(commit=True)
        #     course = Course.objects.get(id=request.POST.get('courseID'))
        #     section.course = course
        #     section.save()


    sections = Section.objects.all()
    form = SectionForm()

    return render(request, 'main/create.html', {'form': form, 'sections': sections})


# @login_required
def add_topic(request):
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=True)
            section = Section.objects.get(id=request.POST.get('sectionID'))
            topic.section = section
            topic.save()

    topics = Topic.objects.all()

    context = {
        'form': form,
        'topics': topics
    }
    return render(request, 'main/topic.html', context)


# @login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=True)
            topic = Topic.objects.get(id=request.POST.get('topicID'))
            question.section = topic
            topic.save()

    questions = Question.objects.all()
    form = QuestionForm()
    context = {
        'form': form,
        'questions': questions
    }
    return render(request, 'main/question.html', context)


# @login_required
def catalog(request):
    return render(request, 'main/catalog.html')


@login_required
def newtest(request):
    return render(request, 'main/newtest.html')


@login_required
def testlist(request):
    return render(request, 'main/testlist.html')






