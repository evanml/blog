from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from .models import Post, Photo, Gallery
from .filters import PhotoFilter
from django.views import View
from django.views.generic import ListView, DetailView


# Create your views here.
def about(request):
    return render(request, 'blog/about.html')

def home(request):
    return render(request, 'blog/home.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


class PhotoListView(ListView):
    model = Photo
    template_name = 'blog/photo_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PhotoFilter(self.request.GET, queryset=self.get_queryset())
        return context



def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'blog/photo_detail.html', {'photo': photo})
