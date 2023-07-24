from rest_framework import generics,permissions

from .models import Profile, Post, Comment, Relationship
from .serializers import ProfileSerializer, PostSerializer, CommentSerializer, RelationshipSerializer,UserSerializer
from rest_framework import filters
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordResetForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
from django.db.models import Q
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                profile = Profile.objects.create(user=user)

            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                try:
                    profile = Profile.objects.get(user=user)
                except Profile.DoesNotExist:
                    profile = Profile.objects.create(user=user)

                return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                subject_template_name='registration/password_reset_subject.txt',
                email_template_name='registration/password_reset_email.html',
                html_email_template_name='registration/password_reset_email.html',
            )
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'bio']  
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(user__username__icontains=search_query) | Q(bio__icontains=search_query))
        return queryset


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'content', 'hashtags']


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'post__content', 'content'] 

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RelationshipListCreateAPIView(generics.ListCreateAPIView):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['follower__username', 'following__username'] 

class RelationshipRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
 