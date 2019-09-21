from django import forms
from .models import Posts

class CreatePost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"
        exclude = ('author', 'created_at',)