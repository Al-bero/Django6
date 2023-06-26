from django.shortcuts import render
# to make this blog visibale to the user :
#1- import the blog(المكان اللي دحين العميل حق الحساب بينزل فيه الشغل اللي نبغاه ينعرض على المتخدمين )
from . models import blog


# Create your views here.
#the name of the function here must be different from the one in modul.py
def blog1(request):
    #2- take a cop
    post=blog.objects.all()
    # this fun. objects takes all contant in the blog and save it in the post 
    #3- send this post the html page by adding new argument in render ,,, {'post':post} == {'value':name}
    return render(request,'blog/blog.html', {'post':post})
   
