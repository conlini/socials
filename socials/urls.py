from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'message_board.views.home', name='home'),
                       url(r'message/', include('mesage_board.urls')),
)
