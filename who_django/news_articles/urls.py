from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.article_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$',views.article_edit, name="article_edit"),
	url(r'^video/$', views.article_video_list, name="article_video_list"),
	url(r'^text/$', views.article_text_list, name="article_text_list"),
]
#url(r'^name/$',views.get_name, name="name"),
