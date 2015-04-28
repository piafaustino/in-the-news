from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.article_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$',views.article_edit, name="article_edit"),
]
#url(r'^name/$',views.get_name, name="name"),
