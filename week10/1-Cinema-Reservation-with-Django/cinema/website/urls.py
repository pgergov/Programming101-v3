from django.conf.urls import patterns, url

urlpatterns=patterns('website.views',
        url(r'^$', 'index'),
        url(r'movies/$', 'movies'),
        url(r'login/$', 'login_tmp', name='login'),
        url(r'submit/$', 'submit', name='submit'),
        url(r'^register/$', 'register'),
        url(r'^logout/$', 'logout_tmp'),
	url(r'^reservation/$', 'reservation'),
	url(r'^get_reserv/$', 'get_reserv'),
	url(r'^completed/$', 'completed')
    )
