from django.shortcuts import render,redirect
from .models import Article
# Create your views here.

from django.views import generic
from django.urls import reverse_lazy

import os
from django.conf import settings
from .models import User

from .forms import SignUpForm,ArticleCreateForm
from . import forms


class IndexView(generic.TemplateView):
    template_name = 'index.html'

class SignUpView(generic.CreateView):
        form_class = SignUpForm
        success_url = reverse_lazy('login')
        template_name = 'signup.html'

class ArticleListView(generic.ListView): # generic の ListViewクラスを継承
    model = Article # 一覧表示させたいモデルを呼び出し

class ArticleCreateView(generic.CreateView): # 追加
    model = Article # 作成したい model を指定
    form_class = ArticleCreateForm # 作成した form クラスを指定
    success_url = reverse_lazy('article_list') # 記事作成に成功した時のリダイレクト先を指定

class ArticleDetailView(generic.DetailView): # 追加
    model = Article  # pk(primary key)はurls.pyで指定しているのでここではmodelを呼び出すだけで済む

class ArticleUpdateView(generic.UpdateView): # 追加
    model = Article
    form_class = ArticleCreateForm # ArticleCreateFormをほぼそのまま活用できる
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(generic.DeleteView): # 追加
    model = Article
    success_url = reverse_lazy('article_list')

def form_view(request):
    if request.method == 'POST':
        form = forms.ArticleCreateForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
       form = forms.ArticleCreateForm()
    return render(request, 'blog/article_form.html', {'form': form})
