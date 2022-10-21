from django import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # If the methode is POST
    if request.method == 'POST':
        form = PostForm(request.POST) 
       # If the form is valid
        if form.is_valid():

          # Yes, Save
            form.save()

          # Redirect to Home
            return HttpResponseRedirect('/')

        else:
          # No, Show error
            return HttpResponseRedirect(form.erros.as_json())



    # Get all, limit = 20
    posts = Post.objects.all()[:20]

    # Show 
    return render(request, 'posts.html', 
                  {'posts' : posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
   