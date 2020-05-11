from django.shortcuts import HttpResponse, get_object_or_404, render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def latest(request):
    latest_articles = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'blog_app/latest.html', {'latest_articles':latest_articles})

def read_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog_app/read.html', {'article':article})

def new_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            HttpResponce('ERROR INVALID FORM')

    return render(request, 'blog_app/edit.html', {'form':form})