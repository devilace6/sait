from django.shortcuts import render, redirect, HttpResponse
from .models import Articles
from .forms import ArticlesForm, CommentForm
from django.views.generic import DetailView,UpdateView, DeleteView
from django.views.generic.edit import FormMixin
import string
from .models import Category
from django.shortcuts import get_object_or_404
from django.views.generic import View

def news_home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    news = Articles.objects.order_by('date')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        news = Articles.objects.filter(category=category)
    return render(request, 'news/news_home.html',
                  {'news': news, 'categories': categories})


class NewsDetail(FormMixin,DetailView):
    model = Articles
    template_name = 'news/details.html'
    context_object_name = 'article'
    form_class = CommentForm
    success_url = '/news'

    def post (self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)



class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news_delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
            form = ArticlesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/news')
            else:
                error = 'При вводе данных были допущены ошибки'
    form = ArticlesForm()
    data = {
        'form': form,
        'error':error
    }
    return render(request,'news/create.html',data)


class Search(View):
    def get (self, request, *args, **kwargs):
        news = Articles.objects.filter(title__icontains=request.GET.get("search"))
        return render (request, 'news/news_home.html',
                        {'news': news,})


def FilterCatalogView(request):
    news = Articles.objects.all()
    if "sort" in request.GET:
        if request.GET.getlist("sort") == ['date']:
            news = news.order_by('date')
        elif request.GET.getlist("sort") == ['title']:
            print(request.GET.getlist("sort"))
            news = news.order_by('title')
        else:
            pass
    return render (request, 'news/news_home.html',
                   {'news': news})





