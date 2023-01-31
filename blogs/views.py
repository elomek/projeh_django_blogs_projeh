from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

def home_list_view(request):
    return render(request, "home.html")



class PostListView(generic.ListView):
    model = Post
    template_name = 'blogs/post_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datatime_modified')



class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'



class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blogs/post_create.html'

class PostUpdateView(generic.UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'blogs/post_create.html'



class PoseDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blogs/post_delete.html'
    success_url = reverse_lazy('post_list')

#def post_list_view(request):
    #posts = Post.objects.filter(status='pub').order_by('-datatime_modified')
    #return render(request,'blogs/post_list.html' ,{'posts':posts})

# def post_detail_view(request, pk):
# post = get_object_or_404(Post, pk=pk)
# return render(request, 'blogs/post_detail.html', {'post': post})


#def post_create_view(request):
    #if request.method == 'POST':
        #form = PostForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('post_list')

    #else :
        #form= PostForm()
    #return render(request,'blogs/post_create.html', context={'form' : form })


# def post_update_view(request, pk):
# post=get_object_or_404(Post ,pk=pk)
# form = PostForm(request.POST or None,instance=post)
# if form.is_valid():
# form.save()
# return redirect('post_list')
# return render(request, 'blogs/post_create.html', context={'form': form})

#def post_delete_view(request, pk):
    #post = get_object_or_404(Post, pk=pk)
    #if request.method == 'POST':
        #post.delete()
        #return redirect('post_list')

    #return render(request, 'blogs/post_delete.html ',context={'post':post})

