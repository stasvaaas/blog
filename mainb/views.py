from django.shortcuts import render, redirect
from django.views import generic
from .models import BlogPost, Topic, Author
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, BlogPostForm


# a function based view
def index(request):
    num_posts = BlogPost.objects.all().count()
    num_authors = Author.objects.all().count()
    num_topics = Topic.objects.count()
    context = {
        'num_posts': num_posts,
        'num_authors': num_authors,
        'num_topics': num_topics,
    }
    return render(request, 'blog.html', context=context)


class PostedByAuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    template_name = 'mainb/author_list_posted.html'

    def get_queryset(self):
        return Author.objects.filter(posted=self.request.user)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            error = 'Form is incorrect'
    form = BlogPostForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', data)


class BlogPostListView(generic.ListView):
    model = BlogPost
    # context_object_name = 'post_list'


class BlogPostDetailView(generic.DetailView):
    model = BlogPost


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class TopicDetailView(generic.DetailView):
    model = Topic


class TopicListView(generic.ListView):
    model = Topic
