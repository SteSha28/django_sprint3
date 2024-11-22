from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Post, Category


def index(request):
    post_list = Post.objects.filter(
        pub_date__lte=now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    instance = get_object_or_404(
        Post,
        pk=id,
        pub_date__lte=now(),
        is_published=True,
        category__is_published=True
    )
    context = {'post': instance}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    post_list = Post.objects.filter(
        pub_date__lte=now(),
        is_published=True,
        category=get_object_or_404(
            Category,
            slug=category_slug,
            is_published=True
        )
    )
    context = {'post_list': post_list}
    return render(request, 'blog/category.html', context)
