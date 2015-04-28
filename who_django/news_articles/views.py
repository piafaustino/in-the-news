from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NewsArticle
from .forms import NewsArticleForm
#from .forms import NameForm

def article_list(request):
	articles = NewsArticle.objects.order_by('date')
	return render(request, 'news_articles/article_list.html', {'articles': articles})

def article_detail(request,pk):
	article = get_object_or_404(NewsArticle, pk=pk)
	return render(request, 'news_articles/article_detail.html', {'article':article})
# Create your views here.

def article_edit(request, pk):
	article = get_object_or_404(NewsArticle, pk=pk)
	if request.method == "POST":
		form = NewsArticleForm(request.POST, instance=article)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('news_articles.views.article_list')
	else:
		form = NewsArticleForm()
	return render(request, 'news_articles/article_edit.html', {'form': form})
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
