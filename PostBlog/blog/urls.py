from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    #path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'), # new

    path('', PostListView.as_view(), name='blog-home'), # new
    path('post/new/', PostCreateView.as_view(), name='blog-new'), # new
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'), # new
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'), # new
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'), # new

]