from django.conf.urls import url

from . import views

app_name = 'seedstars'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add$', views.AddView.as_view(), name='add'),
    url(r'^list$', views.ListView.as_view(), name='list')
]