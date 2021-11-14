from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from .utils import searchBlogs,paginateBlogs
from .models import *
from .forms import *
# Create your views here.
def blogs(request):
    tags = Tag.objects.all()
    d={}
    blogs = Blog.objects.all()
    for i in blogs:
        tags_in_i = i.tags.all()
        for j in tags_in_i:
            d[j.name]=d.get(j.name,0)+1

    blogs, search_query = searchBlogs(request)
    custom_range, blogs = paginateBlogs(request, blogs, 6)
    context = {'blogs':blogs,'search_query':search_query,'custom_range': custom_range,'tags':d}
    return render(request,'blogs/blogs.html',context)

def blog(request,pk):
    blogObj = Blog.objects.get(id=pk)

    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.blog = blogObj
        review.owner = request.user.profile
        review.save()

        blogObj.getVoteCount

        messages.success(request,'Your review was successfully submitted')
        return redirect('blog',pk=blogObj.id)

    context={'blog':blogObj,'form':form}
    return render(request,'blogs/single-blog.html',context)

@login_required(login_url='login')
def createblog(request):
    profile = request.user.profile
    form = BlogForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        form = BlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = profile
            blog.save()
            form.save_m2m()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                blog.tags.add(tag)
            return redirect('account')

    context = {'form': form}
    return render(request, "blogs/blog_form.html", context)

@login_required(login_url='login')
def updateblog(request,pk):
    profile = request.user.profile
    blog = profile.blog_set.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()

        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                blog.tags.add(tag)

            return redirect('account')

    context = {'form': form, 'blog': blog}
    return render(request,'blogs/blog_form.html',context)

@login_required(login_url='login')
def deleteBlog(request,pk):
    profile = request.user.profile
    blog = profile.blog_set.get(id=pk)
    if request.method=='POST':
        blog.delete()
        return redirect('account')
    context={'object':blog}
    return render(request,'delete_template.html',context)