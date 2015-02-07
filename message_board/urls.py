from django.conf.urls import patterns, url


urlpatterns = patterns("",
                       url(r'^message/save$', 'views.save_message'),
                       url(r'^question/(\w+)/$', 'views.get_messages'),
                       url(r'^question/save$', 'views.save_question'),
                       url(r'^topic/(\w+)$', 'views.get_questions'))