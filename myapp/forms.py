from django import forms
from .models import Blogs
class BlogForm(forms.Form):
    name = forms.CharField(max_length=255,required=False)
    topic = forms.CharField(max_length=255,required=False)
    date = forms.DateField(required=False)
    addition_info = forms.CharField(max_length=255,required=False)