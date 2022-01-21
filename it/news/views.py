from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView,UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('date')
    return render(request, 'news/news_home.html',{'news': news})

class NewsDetail(DetailView):
    model = Articles
    template_name = 'news/details.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news_delete.html'



def create(request):
    error =''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        print(form.errors)
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

