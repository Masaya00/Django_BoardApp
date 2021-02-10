from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import ModelFormMixin

# Create your views here.

class PostFormView(ListView, ModelFormMixin):
    model = Post
    template_name = 'Board_App/post_list.html'
    form_class = PostForm
    success_url = reverse_lazy('Board_App:post_list')

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



class CommentFormView(ListView, ModelFormMixin):
    model = Comment
    template_name = 'Board_App/post_comment.html'
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def comment(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        post_pk = self.kwargs['pk']
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('Board_App:post_comment', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_pk = self.kwargs['pk']
        context['post'] = get_object_or_404(Post, pk=post_pk)
        return context

