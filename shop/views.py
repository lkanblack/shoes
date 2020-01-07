from django.shortcuts import render
from .models import Post

def shop_list(request):
    posts = Post.objects.all()
    return render(request, 'shop/shop_list.html', {'posts': posts})
