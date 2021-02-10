from django.forms import ModelForm, TextInput, Textarea
from .models import Post, Comment

class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ('title',)
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'スレッド名',
            }),
        }

        labels = {
            'author': 'スレッド名',
        }

class CommentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ニックネーム'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': '本文'
            }),
        }

        labels = {
            'author': 'ニックネーム',
            'text': '本文'
        }