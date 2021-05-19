from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def blogList(request):
    blogs = Blog.objects.all() #쿼리셋
    return render(request, 'blogList.html', {'blogs': blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})

def introduce(request):
    return render(request, 'introduce.html')

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form' : form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail' , new_blog.id)
    return redirect('home')
    # blog = Blog()
    # blog.title = request.POST['title']
    # blog.writer = request.POST['writer']
    # blog.body = request.POST['body']
    # blog.pub_date = timezone.now()
    # blog.image = request.FILES['image']
    # blog.save()
    # return redirect('detail' , blog.id)
    

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail' , update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('blogList')