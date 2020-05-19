from django.shortcuts import HttpResponse, get_object_or_404, render, get_list_or_404, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django import forms
from django.db.models import Q
from .models import Article, Comment, Category, Tag
from .forms import ArticleForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                   UpdateView, DeleteView )


##########################################################
#-------------------------ARTICOLI-----------------------#
class ArticleListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['pin_articles'] = get_list_or_404(Article, pin=True, pub_date__isnull=False)
        context['categories'] = get_list_or_404(Category)
        context['tags'] = get_list_or_404(Tag)
        return context

    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

def search_article(request):
    print(request)
    if request.method == 'POST':
        print(request.POST['search'])
        search =forms.CharField(max_length=100)
        value = search.clean(request.POST['search'])
        # TODO gestione errori per la validazione
        return redirect('blog_app:search_article', search=value)
    else:
        return redirect('index')

class ArticleSearchView(ListView):
    model=Article

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['pin_articles'] = get_list_or_404(Article, pin=True, pub_date__isnull=False)
        context['categories'] = get_list_or_404(Category)
        context['tags'] = get_list_or_404(Tag)
        context['search'] = self.kwargs['search']
        return context
    
    def get_queryset(self):
        return Article.objects.filter(Q(title__icontains=self.kwargs['search'])|Q(content__icontains=self.kwargs['search'])).order_by('-pub_date')


class CategoryListView(ListView):
    template_name = 'blog_app/article_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['pin_articles'] = get_list_or_404(Article, pin=True, pub_date__isnull=False)
        context['category'] = self.category
        context['categories'] = get_list_or_404(Category)
        context['tags'] = get_list_or_404(Tag)
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, cat_name=self.kwargs['category'])
        return Article.objects.filter(category=self.category).order_by('-pub_date')

class TagListView(ListView):
    template_name = 'blog_app/article_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['pin_articles'] = get_list_or_404(Article, pin=True, pub_date__isnull=False)
        context['tag'] = self.tag
        context['categories'] = get_list_or_404(Category)
        context['tags'] = get_list_or_404(Tag)
        return context

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, tag_name=self.kwargs['tag'])
        return Article.objects.filter(tag=self.tag).order_by('-pub_date')

class ArticleDetailView(DetailView):
    model = Article

class CreateArticleView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/article_detail.html'
    form_class = ArticleForm
    model = Article

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/article_detail.html'
    form_class = ArticleForm
    model = Article

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/article_drafts_list.html'
    model = Article
    template_name = 'blog_app/article_drafts_list.html'

    def get_queryset(self):
        return Article.objects.filter(pub_date__isnull=True).order_by('create_date')

@login_required
def article_publish(request,pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('blog_app:article_detail', pk=pk)

##########################################################
#-------------------------COMMENTI-----------------------#

@login_required
def add_comment_to_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # ! capire cosa fa commit di preciso # TODO leggi qui https://www.tutlane.com/tutorial/sqlite/sqlite-transactions-begin-commit-rollback
            comment.article = article
            comment.save()
            return redirect('blog_app:article_detail', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'blog_app/comment_form.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog_app:article_detail', pk = comment.article.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    article_pk = comment.article.pk
    comment.delete()
    return redirect('blog_app:article_detail', pk = article_pk)