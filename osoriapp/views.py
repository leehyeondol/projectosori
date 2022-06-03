from django.shortcuts import get_object_or_404, render,redirect
from .forms import postform
from .models import Post

def home(request):
    return render(request,'index.html')

def annonyboard(request):

    posts = Post.objects.filter().order_by('-date')
    return render(request,'anonyboard.html',{'posts':posts})


def fashionboard(request):
    return render(request,'fashionboard.html')


def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('annoyboard')
    else:
        form=postform()
    return render(request,'post_form.html',{'form':form})    

def detail(request,post_id):
    post_detail=get_object_or_404(Post,pk=post_id)
    return render(request,'detail.html',{'post_detail':post_detail})