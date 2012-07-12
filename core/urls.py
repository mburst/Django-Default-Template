from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('core.views',
    url(r'^$', 'home', name='home'),
    #url(r'^blog/(?P<slug>.*)/$', 'entry', name='entry'),
    #url(r'^portfolio/', TemplateView.as_view(template_name="core/portfolio.html")),
)