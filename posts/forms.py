from django import forms
from .models import Posts, Comment


class CreatePost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"
        exclude = ('author', 'created_at','likes')

        widgets = {

            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'slug' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
        'text': ''
    }
        widgets = {

            'text'  : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Place Your Comment Here',}) 
        }

