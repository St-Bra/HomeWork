from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from django.utils import timezone

def post_list_json(request):

    posts = Post.objects.filter(deleted_at__isnull = True)

    posts_list = list(posts.values('id', 'title', 'content', 'created_at'))

    return JsonResponse(posts_list, safe=False)


def post_detail_json(request, pk):
    try:
        post = Post.objects.filter(pk=pk, deleted_at__isnull=True).values('id', 'title', 'content', 'created_at').first()

        if post is None:
            return JsonResponse({'error': 'Post not found'}, status=404)

        return JsonResponse(post)

    except Exception as e:
        return JsonResponse({'error': 'Something went wrong'}, status=500)


def post_list_html(request):
    posts = Post.objects.filter(deleted_at__isnull=True).order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail_html(request, pk):
    post = get_object_or_404(Post, pk=pk, deleted_at__isnull=True)
    return render(request, 'blog/post_detail.html', {'post':post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.deleted_at = timezone.now()
    post.save()
    return redirect('post-list-html')












