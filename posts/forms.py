from django import forms
from .models import Posts, Comment


class CreatePost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"
        exclude = ('author', 'created_at',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
