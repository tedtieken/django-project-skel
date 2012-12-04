from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('{{ project_name }}.misc.views',
  url(r'^$', 'home', name='home'),
)
