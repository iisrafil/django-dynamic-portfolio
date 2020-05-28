from django.shortcuts import render

# Create your views here.
def all_blog(request):
    return render(request, 'blog/all_blog.html')