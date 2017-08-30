from django.conf.urls import url
from . import views
app_name = 'detail'
urlpatterns = [
    #url(r'^$', views.Index.as_view()),
    #url(r'^del/(\d+)$', views.delete),
    url(r'^(?P<pk>[0-9]+)/$', views.CarView.as_view(), name='car'),
    # url(r'^del/(\d+)$', views.delete, name='delete'),
]