
from django.shortcuts import get_object_or_404, render

from blog.models import Post

# Create your views here.



def post_list(request):
     posts=Post.objects.all()
     return render(request,'blog/post/list.html',{'posts':posts})
def post_detail(request,id):
     #method 1
     # try:
     #      post=Post.objects.get(id=id)
     # except Post.DoesNotExist:
     #      raise Http404("No Post found")     
     # return render(request,'blog/post/detail.html',{'post':post})

    #methode 2
    post =get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    return render(request,'blog/post/detail.html',{'post':post})