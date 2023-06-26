from .import views
from django.urls import path

urlpatterns = [
    path('blog',views.blog1,name='blog')
    # blog1 == is the name of the function in view
    ]
