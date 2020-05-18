from django.shortcuts import HttpResponse, get_object_or_404, render, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Article, Comment
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
        context['pin_articles'] = get_list_or_404(Article, pin=True)
        return context

    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

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
    redirect_field_name = 'blog/article_list' # ! vedere se si può mettere solo il namespace 'article_list'
    model = Article

    def get_queryset(self):
        return Article.objects.filter(pub_date__isnull=True).order_by('create_date')

@login_required
def article_publish(request,pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('article_detail', pk=pk)

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
            return redirect('article_detail', pk=article.pk)
        else:
            form = CommentForm()
    return render(request, 'blog_app/comment_form.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('article_detail', pk = comment.article.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    article_pk = comment.article.pk
    comment.delete()
    return redirect('article_detail', pk = article_pk)