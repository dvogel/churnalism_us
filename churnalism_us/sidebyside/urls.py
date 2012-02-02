from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('sidebyside.views',
    # Examples:
    # url(r'^$', 'sfm_us_site.views.home', name='home'),
    # url(r'^sfm_us_site/', include('sfm_us_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'search_page', name='sidebyside-search-page'),
    url(r'^search/$', 'search', name='sidebyside-search'),
)
