from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from models import Message
from forms.UserForms import RegisterForm
from forms import MessageForm, CommentForm
from django.http import Http404


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
    else:
        out['register_form'] = RegisterForm()
        out['login_form'] = AuthenticationForm()

    return render(request, template_return, out)


@login_required(login_url='/login')
def save_comment(request, msg_pk):
    if request.POST:
        message = Message.objects.get(pk=msg_pk)
        form = CommentForm(message, user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/socials/message/{}".format(msg_pk,))
        else:
            return render(request, "message_board/message.html",
                          {"message": message,
                           "comment_form": form})


@login_required(login_url='/login')
def save_message(request):
    if request.method == "POST":
        form = MessageForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "message_board/new_message.html",
                          {"new_msg_form": form})
    return redirect("home")


def get_messages(request, topic):
    msgs = Message.objects.filter(topic_id=topic)
    return render(request, "message_board/home.html", {"messages" : msgs})


def get_comments(request, msg_pk):
    message = Message.objects.get(pk=msg_pk)
    comment_form = CommentForm(message)
    return render(request, "message_board/message.html",
                  {"message": message, "comment_form": comment_form})


def log_me_in(request):
    out = {}
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        else:
            return render(request, "message_board/pie_base.html",
                          {"login_form": form,
                           "register_form": RegisterForm()})
    return redirect("home")


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.clean_username()
            passwd = register_form.clean_password2()
            user = register_form.save(True)
            u = authenticate(username=username, password=passwd)
            login(request, u)
        else:
            return render(request, "message_board/pie_base.html",
                          {"register_form": register_form,
                           "login_form": AuthenticationForm()})
    return redirect("home")


def log_me_out(request):
    logout(request)
    return redirect("home")


@login_required(login_url="/login")
def new_message(request):
    return render(request, "message_board/new_message.html",
                  {"new_msg_form": MessageForm()})