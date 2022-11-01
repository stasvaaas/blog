from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, BlogPost, BlogComment
from django.forms import ModelForm, TextInput


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['topic', 'title', 'main_text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'topic': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Topic'
            }),
            'main_text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your text...'
                })
        }


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content']