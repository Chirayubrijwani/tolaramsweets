from django.conf.urls import url
from . import views 
app_name = 'home'
urlpatterns = [
    url(r'^$', views.home,name="index"),
    url(r'^tolaram/menu/$', views.menu,name="menu"),
    url(r'^tolaram/blog/$', views.blog,name="blog"),
    url(r'^tolaram/contact/$', views.contact,name="contact"),
    url(r'^tolaram/events/$', views.events,name="events"),
    url(r'^tolaram/menu/(?P<id>\d+)/$', views.variety,name="variety"),

]
