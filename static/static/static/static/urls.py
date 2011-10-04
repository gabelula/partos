from django.conf.urls.defaults import patterns, include, url
from partouy.births.views import home, about, contact, thanks, post_birth, thanks_birth, get_birth
from births.api import BirthResource
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Register the api
v1_api = Api(api_name=('v1'))
v1_api.register(BirthResource())

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^nosotras/', about),
    url(r'^contacto/', contact),
    url(r'^gracias/$', thanks),
    url(r'^gracias/por/tu/historia/', thanks_birth),
    # displaying a story
    url(r'^historia/([a-zA-Z0-9-]+)/$', get_birth),
    # sending a story throught the form
    url(r'^tu_historia/', post_birth),
    # captcha for the forms
    url(r'^captcha/', include('captcha.urls')),
    # tinymce editor
    url(r'^tinymce/', include('tinymce.urls')),

    # api 
    (r'^api/',include(v1_api.urls)),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(site.urls)),
)
