from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import GonderiForm

def gonderi_list(request):
    posts = Post.objects.filter(yayinlama_tarihi__lte=timezone.now()).order_by('yayinlama_tarihi')
    return render(request, 'blog/post_list.html', {'posts': posts})

def gonderi_detay(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def gonderi_duzenle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = GonderiForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.yazar = request.user
            post.yayinlama_tarihi = timezone.now()
            post.save()
            return redirect('blog.views.gonderi_detay', pk=post.pk)
    else:
        form = GonderiForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})



def yeni_gonderi(request):
    if request.method == "POST":
        form = GonderiForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.yazar = request.user
            post.yayinlama_tarihi = timezone.now()
            post.save()
            return redirect('blog.views.gonderi_detay', pk=post.pk)
    else:
        form = GonderiForm()
    return render(request, 'blog/post_edit.html', {'form': form})