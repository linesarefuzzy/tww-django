from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Uncomment the admin/doc line below to enable admin documentation:
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),

	# (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'accounts/login.html'}),
	# (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
	# (r'^accounts/logout/$', 'loans.views.logout_view'),
)

urlpatterns += patterns('loans.views',
	(r'^$', 'home'),
	(r'^loans/$', 'loans'),
	(r'^loans/(?P<loan_id>\d+)/$', 'loan_detail'),
	(r'^loans/(?P<loan_id>\d+)/lend$', 'lend_form'),
	(r'^accounts/login/$', 'login_view'),
	(r'^accounts/logout/$', 'logout_view'),
	(r'^accounts/profile/$', 'user_profile'),
)
