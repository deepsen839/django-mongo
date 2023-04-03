from django.shortcuts import render
from .forms import BlogForm
from .models import Blogs
# Create your views here.
def my_view(request):
    form = BlogForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            name = form.cleaned_data["name"]
            topic = form.cleaned_data["topic"]
            date = form.cleaned_data["date"]
            addition_info = form.cleaned_data["addition_info"]
            blog = Blogs(name=name,topic=topic,date=date,addition_info=addition_info) 
            blog.save()
    return render(request,'test.html',{'form':form})        
