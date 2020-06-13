from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


def home(request):
    context = {
        'posts':Posts.objects.all()
        }
    
    return render(request,'index.html',context)


# Listview,DetailView,UpdateView,DeleteView,CreateView these are the Generic classes 
# Provided by the django which have in built views we just need to import them
# And use them. Here we used these to display the posts ,create and delete the posts  

class PostListView(ListView):
    model = Posts
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']



class PostdetailView(DetailView):
    model = Posts
    
# loginrequired mixin is used to make sure that if a person is not logged in he cannot access these functions 

class PostcreateView(LoginRequiredMixin,CreateView):
    model = Posts
    fields = ['title','content','image','video','video_enable']

    def get_form(self, form_class=None):
        form = super(PostcreateView, self).get_form(form_class)
        form.fields['video'].required = False
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# loginrequired mixin is used to make sure that if a person is not logged in he cannot access these functions 
# userpasses test is like giving the permissions to use these functions only to those posts which belog to them  
# everyone cannot access these funtions ,they can access only their posts functions ,not others

class PostupdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Posts
    fields = ['title','content','image','video','video_enable']
    

    def get_form(self, form_class=None):
        form = super(PostupdateView, self).get_form(form_class)
        form.fields['video'].required = False
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    
    

class PostdeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Posts
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False