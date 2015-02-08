from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def home(request):
    # simple page with login
    # if login, show categories and last 10 topics discussed
    return render(request, 'message_board/home.html')


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
    out = {}
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("password")
        u = authenticate(username=username, password=passwd)
        if u:
            login(request, u)
        else:
            out.update({"login_error": "Invalid username/passoword"})
    return render(request, "message_board/home.html", out)



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get('password')
        email = request.POST.get('email')
        u = User();
        u.set_password(passwd)
        u.username = username
        u.is_active = True
        u.email = email
        u.save();
        u = authenticate(username=u.username, password=passwd)
        login(request, u)
    return render(request, "message_board/home.html")





