from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NewsArticle
from .forms import NewsArticleForm
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
	print test_dict.keys()
	for key in test_dict.keys():
		dict_val = test_dict[key]
		print type(dict_val), dict_val
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
	if request.method == "POST":
		form = NewsArticleForm(request.POST)
		if form.is_valid():
			print "CLEANED DATA"
			pprint(form.cleaned_data)
			NewsArticle.objects.filter(pk=pk).update(**form.cleaned_data)
			return redirect('news_articles.views.article_list')
	else:
		article_dict = to_dict(article)
		article_dict = string_to_list(article_dict)
		print "OUTPUT DATA"
		pprint(article_dict)

		news_type = article.news_type

		form = NewsArticleForm(article_dict)

		try:
			prev_article_pk = NewsArticle.objects.filter(order_id__lt=article.order_id).order_by('order_id')[0].pk
		except Exception, e:
			print e
			prev_article_pk = article.pk

		try:
			next_article_pk = NewsArticle.objects.filter(order_id__gt=article.order_id).order_by('order_id')[0].pk
		except Exception, e:
			print e
			next_article_pk = article.pk

	return render(request, 'news_articles/article_edit.html', {'form': form,
															   'article':article,
															   'prev_article_pk':prev_article_pk,
															   'next_article_pk':next_article_pk
															   })

'''
def get_name(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether its valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required.
			# ...
			# redirect to a new URL:
			name = form.cleaned_data['your_name']
	else:
		form = NameForm()
		name = ''
	return render(request, 'news_articles/name.html',{'form':form,'current_name': 'dog','name':name})
'''
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
