
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),  
    path('profiles/', views.ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', views.ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-retrieve-update-destroy'),
    path('posts/', views.PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),
    path('comments/', views.CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-retrieve-update-destroy'),
    path('relationships/', views.RelationshipListCreateAPIView.as_view(), name='relationship-list-create'),
    path('relationships/<int:pk>/', views.RelationshipRetrieveUpdateDestroyAPIView.as_view(), name='relationship-retrieve-update-destroy'),
]
