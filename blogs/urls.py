from django.urls import path
from . import views
urlpatterns = [
    path('',views.blogs,name='blogs'),
    path('blog/<str:pk>/',views.blog,name='blog'),
    path('create-blog/',views.createblog,name='create-blog'),
    path('update-blog/<str:pk>/',views.updateblog,name='update-blog'),
    path('delete-blog/<str:pk>/',views.deleteBlog,name='delete-blog')
]
