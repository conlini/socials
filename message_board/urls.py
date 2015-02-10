from django.conf.urls import patterns, url
from message_board import views as views

urlpatterns = patterns("message_board.views",
                       url(r'^comment/(\d+)/save$', 'save_comment'),
                       url(r'^message/(\w+)/$', 'get_comments'),
                       url(r'^message/save$', 'save_message'),
                       url(r'^topic/(\w+)$', 'get_messages'),
                       url(r'^new_message$', 'new_message'))
