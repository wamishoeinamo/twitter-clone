

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from .models import Post
from .forms import PostForm


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
         # If the form is valid
        if form.is_valid():
              # Yes, Save
            form.save()
              # Redirect to Home
            return HttpResponseRedirect('/')
        else:
              # No, Show Error
            return HttpResponseRedirect(form.error.as_json())
    #Get all posts, Limit = 20

    posts = Post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'Posts.html',
                {'posts':posts})

def delete(request, post_id):
   
     post = Post.objects.get(id=post_id)
     post.delete()
     return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "edit.html", {"post": post})
    if request.method == "POST":
        editposts = Post.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=editposts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")


def LikeView(request, post_id):
  new_value = Post.objects.get(id=post_id)
  new_value.likes += 1
  new_value.save()
  return HttpResponseRedirect('/')

    
                   

