from django.shortcuts import render,get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post
import json

@login_required
@require_POST
def post_like(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = post.likes.filter(id = request.user.id).exists()
    if is_liked :
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', kwargs = {'post_id':post.id}))

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    is_liked = False

    if post.likes.filter(id = request.user.id).exists():
        is_liked = True
    
    return render(request, 'post_detail.html', context = {'post':post, 
    'is_liked':is_liked, 'total_likes':post.total_likes()})


def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'post_list.html', context = {'posts':posts})


@login_required
def post_write(request):
    errors = []
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        image = request.FILES.get('image')

        if not title:
            errors.append('제목을 입력하세요.')
        if not content:
            errors.append('내용을 입력하세요.')

        if not errors:
            post = Post.objects.create(user=request.user, title = title, content = content, image = image)
            return render(request, 'post_list.html')
    return render(request, 'post_write.html', {'user':request.user, 'errors' : errors})
