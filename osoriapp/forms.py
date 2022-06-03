from django import forms
from .models import Post

class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        #fields ={'title','body'}