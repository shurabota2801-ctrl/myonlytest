from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.urls import reverse

def post_list(request):
    pass