from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'message_board.views.home', name='home'),
                       url(r'socials/', include('message_board.urls')),
                       url(r'login', 'message_board.views.log_me_in',
                           name='login'),
                       url(r'register', 'message_board.views.register',
                           name='register'),
                       url(r'logout', 'message_board.views.log_me_out',
                           name='logout'),
)
