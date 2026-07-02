from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from .models import Category, News
from .forms import CategoryForm, NewsForm


def home_page(request):
    latest_news = News.objects.order_by('-published_at')[:3]
    context = {
        'latest_news': latest_news,
    }
    return render(request, 'index.html', context)


def contact_page(request):
    return render(request, 'contact.html')


class CategoryNewsView(ListView):
    model = News
    template_name = "category.html"
    context_object_name = "news_list"

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs["slug"],
        )
        return News.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()

    return render(request, 'category_create.html', {'form': form})


def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()

    return render(request, 'news_create.html', {'form': form})
