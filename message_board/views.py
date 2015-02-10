from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from models import Message


# Create your views here.


def home(request):
    # simple page with login
    # if login, show categories and last 10 topics discussed
    out = {}
    messages = None
    template_return = 'message_board/pie_base.html'
    if request.user.is_authenticated():
        # we are logged in, pull top 10 messages
        messages = Message.objects.all()[:10]
        if messages:
            out["messages"] = messages
        template_return = "message_board/home.html"

    return render(request, template_return, out)


@login_required(login_url='/login')
def save_message(request):
    pass


@login_required(login_url='/login')
def save_question(request):
    if request.method == "POST":
        message_string = request.POST.get('message')
        message = Message()
        message.message = message_string
        message.user = request.user
        message.save()
    return redirect("home")


def get_questions(request, topic):
    pass


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
            out.update({"login_error": "Invalid username/password"})
            return render(request, "message_board/pie_base.html", out)
    return redirect("home")


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
    return redirect("home")


def log_me_out(request):
    logout(request)
    return redirect("home")


def new_message(request):
    return render(request, "message_board/new_message.html")