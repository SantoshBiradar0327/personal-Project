from django.urls import path
from BLOG import views

app_name = "BLOG"

urlpatterns = [
    
    path('', views.blog ,name='all_blogs' ),
   path('<int:blog_id>/', views.detail, name='detail' )

    
]