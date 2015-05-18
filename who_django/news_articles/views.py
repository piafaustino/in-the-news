from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NewsArticle
from .forms import NewsArticleForm, ListFiltersForm
from django.forms.models import model_to_dict
from django.db.models.fields.related import ManyToManyField
from pprint import pprint
import ast
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.http import HttpResponse

#from .forms import NameForm
def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
        else:
            data[f.name] = f.value_from_object(instance)
    return data

def string_to_list(input_dict):
	test_dict = input_dict
	for key in test_dict.keys():
		dict_val = test_dict[key]
		try:
			dict_val = ast.literal_eval(dict_val)
			test_dict[key] = dict_val
		except Exception, e:
			print e
	return test_dict

def article_list(request):
	articles_list = NewsArticle.objects.order_by('order_id')
	paginator = Paginator(articles_list, 10) # show 10 contacts per page

	page = request.GET.get('page') #still have to check what this does.
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		#If page is not an integer, deliver first page.
		articles = paginator.page(1)
	except EmptyPage:
		#If page is out of range(e.g. 9999), deliver last page of results.
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles})

def article_video_list(request):
	articles_list = NewsArticle.objects.filter(news_type__startswith="video")\
					.order_by('relevance_ranking').reverse()
	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html',{'articles': articles})

def article_text_list(request):
	articles_list = NewsArticle.objects.filter(news_type__startswith="text")\
					.order_by('relevance_ranking').reverse()
	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html',{'articles': articles})

def article_exclude_list(request):
	articles_list = NewsArticle.objects.filter(exclude__startswith="Yes")\
					.order_by('relevance_ranking').reverse()
	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles})


def article_include_list(request):
	articles_list = NewsArticle.objects.exclude(exclude__startswith="Yes")\
					.order_by('relevance_ranking').reverse()
	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles})

def article_detail(request,pk):
	article = get_object_or_404(NewsArticle, pk=pk)
	return render(request, 'news_articles/article_detail.html', {'article':article})

def article_edit(request, pk):
	article = get_object_or_404(NewsArticle, pk=pk)
	save_message = None

	if request.method == "POST":
		form = NewsArticleForm(request.POST)
		if form.is_valid():
			print "CLEANED DATA"
			pprint(form.cleaned_data)
			NewsArticle.objects.filter(pk=pk).update(**form.cleaned_data)

			article = get_object_or_404(NewsArticle, pk=pk)
			save_message = "Survey successfully saved."

	article_dict = to_dict(article)
	article_dict = string_to_list(article_dict)

	print "OUTPUT DATA"
	print type(article_dict)
	pprint(article_dict)

	form = NewsArticleForm(article_dict)
	print "FORM"
	print form
	#this part is for the page navigator
	try:
		prev_article_pk = NewsArticle.objects.filter(order_id__lt=article.order_id).order_by('order_id')[0].pk
	except Exception, e:
		prev_article_pk = article.pk

	try:
		next_article_pk = NewsArticle.objects.filter(order_id__gt=article.order_id).order_by('order_id')[0].pk
	except Exception, e:
		next_article_pk = article.pk

	return render(request, 'news_articles/base_filter_edit.html', {'form': form,
															   'article':article,
															   'article_dict':article_dict,
															   'prev_article_pk':prev_article_pk,
															   'next_article_pk':next_article_pk,
															   'save_message':save_message})

def base_filter(request):
	default_articles = NewsArticle.objects.order_by('order_id')
	if request.method == "POST":
		clean = request.POST
		pprint(clean)
		object_caller_list = []

		checked_dict = {}
		list_of_lists = [default_articles]
		#filter field: rater
		if request.POST.get('mavie'):
			rater_count = 1
			mavie_list = NewsArticle.objects.filter(rater__startswith="mavie")
			object_caller_list.append('mavie_list')
			object_caller_list.append('rater_count')
			mavie_checked = 'checked'
		else:
			mavie_list = []
			mavie_checked = None
		if request.POST.get('candice'):
			rater_count = 1
			candice_list = NewsArticle.objects.filter(rater__startswith="candice")
			object_caller_list.append('candice_list')
			object_caller_list.append('rater_count')
			candice_checked = 'checked'
		else:
			candice_list = []
			candice_checked = None
		if request.POST.get('pia'):
			rater_count = 1
			pia_list = NewsArticle.objects.filter(rater__startswith="pia")
			object_caller_list.append('pia_list')
			object_caller_list.append('rater_count')
			pia_checked = 'checked'
		else:
			pia_list = []
			pia_checked = None
		rater_list = list(chain(mavie_list, candice_list, pia_list))

		try:
			if rater_count:
				list_of_lists.append(rater_list)
		except Exception, e:
			print e

		#filter field: completed filter
		if request.POST.get('complete_yes'):
			complete_count = 1
			complete_yes = NewsArticle.objects.filter(completed__startswith="Yes")
			object_caller_list.append('complete_yes')
			object_caller_list.append('complete_count')
			complete_yes_checked = 'checked'
		else:
			complete_yes = []
			complete_yes_checked = None
		if request.POST.get('complete_no'):
			complete_count = 1
			complete_no = NewsArticle.objects.exclude(completed__startswith="Yes")
			object_caller_list.append('complete_no')
			object_caller_list.append('complete_count')
			complete_no_checked = 'checked'
		else:
			complete_no = []
			complete_no_checked = None
		complete_list = list(chain(complete_yes, complete_no))

		try:
			if complete_count:
				list_of_lists.append(complete_list)
		except Exception, e:
				print e

		#filter field: exclude filter
		if request.POST.get('exclude_yes'):
			exclude_count = 1
			exclude_yes = NewsArticle.objects.filter(exclude__startswith="Yes")
			object_caller_list.append('exclude_yes')
			object_caller_list.append('exclude_count')
			exclude_yes_checked = 'checked'
		else:
			exclude_yes = []
			exclude_yes_checked = None
		if request.POST.get('exclude_no'):
			exclude_count = 1
			exclude_no = NewsArticle.objects.exclude(exclude__startswith="Yes")
			object_caller_list.append('exclude_no')
			object_caller_list.append('exclude_count')
			exclude_no_checked = 'checked'
		else:
			exclude_no = []
			exclude_no_checked = None
		exclude_list = list(chain(exclude_yes, exclude_no))

		try:
			if exclude_count:
				list_of_lists.append(exclude_list)
		except Exception, e:
				print e

		#filter field: video filter
		if request.POST.get('video'):
			video_count = 1
			video = NewsArticle.objects.filter(news_type__startswith="video")
			object_caller_list.append('video')
			object_caller_list.append('video_count')
			video_checked = 'checked'
		else:
			video = []
			video_checked = None
		video_list = list(chain(video))

		try:
			if video_count:
				list_of_lists.append(video_list)
		except Exception, e:
				print e

		#filter field: exclude filter
		if request.POST.get('text'):
			text_count = 1
			text = NewsArticle.objects.filter(news_type__startswith="text")
			object_caller_list.append('text')
			object_caller_list.append('text_count')
			text_checked = 'checked'
		else:
			text = []
			text_checked = None
		text_list = list(chain(text))

		try:
			if text_count:
				list_of_lists.append(text_list)
		except Exception, e:
				print e


		#to get the intersection
		articles = set.intersection(*map(set, list_of_lists))
		articles = sorted(articles, key=lambda article: article.order_id) #to sort the list in an ascending order based on the order_id

		object_caller_list = list(set(object_caller_list))
		try:
			articles = object_caller(object_caller_list)
		except TypeError:
			articles = default_articles
			request.session.flush()

		paginator = Paginator(articles, 10)
		page = request.GET.get('page')
		try:
			articles = paginator.page(page)
		except PageNotAnInteger:
			articles = paginator.page(1)
		except EmptyPage:
			articles = paginator.page(paginator.num_pages)

		request.session['session_search_list'] = object_caller_list
		request.session['mavie_checked'] = mavie_checked
		request.session['candice_checked'] = candice_checked
		request.session['pia_checked'] = pia_checked
		request.session['complete_yes_checked'] = complete_yes_checked
		request.session['complete_no_checked'] = complete_no_checked
		request.session['exclude_yes_checked'] = exclude_yes_checked
		request.session['exclude_no_checked'] = exclude_no_checked
		request.session['video_checked'] = video_checked
		request.session['text_checked'] = text_checked


		return render(request, 'news_articles/base_filter_list.html',{'articles':articles,
																 'mavie_checked':mavie_checked,
																 'candice_checked':candice_checked,
																 'pia_checked': pia_checked,
																 'complete_yes_checked':complete_yes_checked,
																 'complete_no_checked':complete_no_checked,
																 'exclude_yes_checked':exclude_yes_checked,
																 'exclude_no_checked':exclude_no_checked,
																 'video_checked':video_checked,
																 'text_checked':text_checked,
																})

	else:

		if request.session.get('session_search_list'):
			articles = object_caller(request.session.get('session_search_list'))
		else:
			articles = default_articles
			request.session.flush()

		#paginator
		paginator = Paginator(articles, 10)
		page = request.GET.get('page')
		try:
			articles = paginator.page(page)
		except PageNotAnInteger:
			articles = paginator.page(1)
		except EmptyPage:
			articles = paginator.page(paginator.num_pages)

		mavie_checked = request.session.get('mavie_checked','')
		candice_checked = request.session.get('candice_checked','')
		pia_checked = request.session.get('pia_checked','')
		complete_yes_checked = request.session.get('complete_yes_checked','')
		complete_no_checked = request.session.get('complete_no_checked','')
		exclude_yes_checked = request.session.get('exclude_yes_checked','')
		exclude_no_checked = request.session.get('exclude_no_checked','')
		video_checked = request.session.get('video_checked','')
		text_checked = request.session.get('text_checked','')

		return render(request, 'news_articles/base_filter_list.html',{'articles':articles,
																 'mavie_checked':mavie_checked,
																 'candice_checked':candice_checked,
																 'pia_checked': pia_checked,
																 'complete_yes_checked':complete_yes_checked,
																 'complete_no_checked':complete_no_checked,
																 'exclude_yes_checked':exclude_yes_checked,
																 'exclude_no_checked':exclude_no_checked,
																 'video_checked':video_checked,
																 'text_checked':text_checked,
																})

def object_caller(filter_list):
	master_list = []
	#rater filter
	if 'rater_count' in filter_list:
		if 'mavie_list' in filter_list:
			mavie_list = NewsArticle.objects.filter(rater__startswith="mavie")
		else:
			mavie_list = []
		if 'candice_list' in filter_list:
			candice_list = NewsArticle.objects.filter(rater__startswith="candice")
		else:
			candice_list = []
		if 'pia_list' in filter_list:
			pia_list = NewsArticle.objects.filter(rater__startswith="pia")
		else:
			pia_list = []
		rater_list = list(chain(mavie_list, candice_list, pia_list))
		master_list.append(rater_list)

	#completed filter
	if 'complete_count' in filter_list:
		if 'complete_yes' in filter_list:
			complete_yes = NewsArticle.objects.filter(completed__startswith="Yes")
		else:
			complete_yes = []
		if 'complete_no' in filter_list:
			complete_no = NewsArticle.objects.exclude(completed__startswith="Yes")
		else:
			complete_no = []
		complete_list = list(chain(complete_yes, complete_no))
		master_list.append(complete_list)

	#exclusion filter
	if 'exclude_count' in filter_list:
		if 'exclude_yes' in filter_list:
			exclude_yes = NewsArticle.objects.filter(exclude__startswith="Yes")
		else:
			exclude_yes = []
		if 'exclude_no' in filter_list:
			exclude_no = NewsArticle.objects.exclude(exclude__startswith="Yes")
		else:
			exclude_no = []
		exclude_list = list(chain(exclude_yes, exclude_no))
		master_list.append(exclude_list)

	#video filter
	if 'video_count' in filter_list:
		if 'video' in filter_list:
			video = NewsArticle.objects.filter(news_type__startswith="video")
		else:
			video = []
		video_list = list(chain(video))
		master_list.append(video_list)

	#text filter
	if 'text_count' in filter_list:
		if 'text' in filter_list:
			text = NewsArticle.objects.filter(news_type__startswith="text")
		else:
			text = []
		text_list = list(chain(text))
		master_list.append(text_list)

	articles = set.intersection(*map(set, master_list))
	articles = sorted(articles, key=lambda article: article.order_id)

	return articles


def testing_post_view(request):
	if request.method == "POST":
		clean = request.POST
		pprint(clean)

		articles = ''
		mavie = None
		if request.POST.get('mavie'):
			print type(request.POST['mavie']), request.POST['mavie']
			articles = NewsArticle.objects.filter(rater__startswith="mavie")

			mavie = request.POST.get('mavie')
			if mavie == u'1':
				mavie = 'checked'
		return render(request, 'news_articles/base_filter.html', {'articles':articles,'mavie':mavie})

	else:

		return render(request, 'news_articles/base_filter.html')

def article_complete_yes_list(request):
	articles_list = NewsArticle.objects.filter(completed__startswith="Yes")\
					.order_by('relevance_ranking').reverse()
	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'complete_yes':1})

def article_complete_no_list(request):
	articles_list = NewsArticle.objects.exclude(completed__startswith="Yes")\
					.order_by('relevance_ranking').reverse()
	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'complete_no':1})

def mavie_list(request):
	articles_list = NewsArticle.objects.filter(rater__startswith="mavie")\
					.order_by('relevance_ranking').reverse()
	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'mavie':1})

def mavie_complete_yes_list(request):
	articles_list = NewsArticle.objects.filter(rater__startswith="mavie")\
					.filter(completed__startswith="Yes").order_by('relevance_ranking').reverse()

	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'mavie_complete_yes':1})

def mavie_complete_no_list(request):
	articles_list = NewsArticle.objects.filter(rater__startswith="mavie")\
					.exclude(completed__startswith="Yes").order_by('relevance_ranking').reverse()

	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'mavie_complete_no':1})

def candice_list(request):
	articles_list = NewsArticle.objects.filter(rater__startswith="candice")\
					.order_by('relevance_ranking').reverse()
	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'candice':1})

def candice_complete_yes_list(request):
	articles_list = NewsArticle.objects.filter(rater__startswith="candice")\
					.filter(completed__startswith="Yes").order_by('relevance_ranking').reverse()

	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'candice_complete_yes':1})

def candice_complete_no_list(request):
	articles_list = NewsArticle.objects.filter(rater__startswith="candice")\
					.exclude(completed__startswith="Yes").order_by('relevance_ranking').reverse()

	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'candice_complete_no':1})

def pia_list(request):
	articles_list = NewsArticle.objects.filter(rater__startswith="pia")\
					.order_by('relevance_ranking').reverse()
	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'pia':1})

def pia_complete_yes_list(request):
	articles_list = NewsArticle.objects.filter(rater__startswith="pia")\
					.filter(completed__startswith="Yes").order_by('relevance_ranking').reverse()

	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'pia_complete_yes':1})

def pia_complete_no_list(request):
	articles_list = NewsArticle.objects.filter(rater__startswith="pia")\
					.exclude(completed__startswith="Yes").order_by('relevance_ranking').reverse()

	paginator = Paginator(articles_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'news_articles/article_list.html', {'articles': articles,'pia_complete_no':1})
