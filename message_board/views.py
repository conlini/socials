from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    # simple page with login
    # if login, show categories and last 10 topics discussed
    render(request, 'message_board/')


@login_required(login_url='/login')
def save_message(request):
    pass


@login_required(login_url='/login')
def save_question(request):
    pass


@login_required(login_url='/login')
def get_questions(request, topic):
    pass


@login_required(login_url='/login')
def get_messages(request, question):
    pass


def log_me_in(request):
    pass


def register(request):
    pass


