from django.shortcuts import render, redirect
from django.views import generic
from .models import BlogPost, Topic, Author, BlogComment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm, BlogPostForm, NewCommentForm


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


class BlogPostListView(generic.ListView):
    model = BlogPost
    # context_object_name = 'post_list'


class BlogPostDetailView(generic.DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        com_title = BlogComment.objects.filter(
            com_title=self.get_object()).order_by('-date_posted')
        data['comments'] = com_title
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content=request.POST.get('content'),
                                  author=self.request.user,
                                  com_title=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class TopicDetailView(generic.DetailView):
    model = Topic


class TopicListView(generic.ListView):
    model = Topic
