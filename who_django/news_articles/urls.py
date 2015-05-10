from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^video/$', views.article_video_list, name="article_video_list"),
	url(r'^text/$', views.article_text_list, name="article_text_list"),
	url(r'^include/$', views.article_include_list, name="article_include_list"),
	url(r'^exclude/$',views.article_exclude_list, name="article_exclude_list"),
	url(r'^complete_yes/$',views.article_complete_yes_list, name="article_complete_yes_list"),
	url(r'^complete_no/$', views.article_complete_no_list, name="article_complete_no_list"),

	url(r'^mavie/$', views.mavie_list, name="mavie_list"),
	url(r'^mavie/complete_yes/$', views.mavie_complete_yes_list, name="mavie_complete_yes_list"),
	url(r'^mavie/complete_no/$', views.mavie_complete_no_list, name="mavie_complete_no_list"),

	url(r'^candice/$', views.candice_list, name="candice_list"),
	url(r'^candice/complete_yes/$', views.candice_complete_yes_list, name="candice_complete_yes_list"),
	url(r'^candice/complete_no/$', views.candice_complete_no_list, name="candice_complete_no_list"),


	url(r'^pia/$', views.pia_list, name="pia_list"),
	url(r'^pia/complete_yes/$', views.pia_complete_yes_list, name="pia_complete_yes_list"),
	url(r'^pia/complete_no/$', views.pia_complete_no_list, name="pia_complete_no_list"),

	url(r'^$',views.base_filter, name="base_filter"),
	url(r'^post/(?P<pk>[0-9]+)/edit/$',views.article_edit, name="article_edit"),

	url(r'^maintest/$', views.testing_post_view, name="testing_view"),
	url(r'^maintest/test/$', views.testing_post_view, name="testing_post_view"),
]
#url(r'^name/$',views.get_name, name="name"),
