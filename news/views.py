from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
from django.contrib import messages


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'news/index.html', context)

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    context = {'post': post, 'posts': posts}
    return render(request, 'news/detail.html', context)

def createPost(request):
    profile = request.user.userprofile
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.writer = profile
            post.save()
            messages.info(request, 'Article created successfully')
            return redirect('create')
        else:
            messages.error(request, 'Article not created')
    context = {'form': form}
    return render(request, 'news/create.html', context)

def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Article updated successfully')
            return redirect('detail', slug=post.slug)
    context = {'form': form}
    return render(request, 'news/create.html', context)

def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        post.delete()
        messages.info(request, 'Article deleted successfully')
        return redirect('create')
    context = {'form': form}
    return render(request, 'news/delete.html', context)
