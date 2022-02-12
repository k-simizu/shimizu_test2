from django.urls import path
from .views import SignUpView,IndexView
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('signup/', views.SignUpView.as_view(),name='signup'),
    path('article_list/', views.ArticleListView.as_view(), name='article_list'), # ここを追加
    path('article_create/', views.form_view, name='article_create'), # 追加
    path('article_detail/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'), # 追加　(例) /blog/detail/1　※特定のレコードに対して処理を行うので pk で識別
    path('article_update/<int:pk>/', views.ArticleUpdateView.as_view(), name='article_update'), # 追加　(例) /blog/update/1　※同上
    path('article_delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='article_delete'), # 追加　(例) /blog/delete/1　※同上
]
