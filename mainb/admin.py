from django.contrib import admin
from .models import BlogPost, Topic, CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm


# ways to register models to admin site

# admin.site.register(BlogPost)
# admin.site.register(Topic)
# admin.site.register(Author)

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
# list_display = ('user_name', 'last_name', 'first_name',)
# fields = ('user_name', 'last_name', 'first_name', 'date_of_birth')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_topic', 'posted')
    list_filter = ('author', 'topic', 'posted')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)
