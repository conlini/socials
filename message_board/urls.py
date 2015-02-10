from django.conf.urls import patterns, url
from message_board import views as views

urlpatterns = patterns("message_board.views",
                       url(r'^comment/save$', 'save_message'),
                       url(r'^message/(\w+)/$', 'get_messages'),
                       url(r'^message/save$', 'save_question'),
                       url(r'^topic/(\w+)$', 'get_questions'),
                       url(r'^new_message$', 'new_message'))
