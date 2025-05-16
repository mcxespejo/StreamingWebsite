from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Banner, Side_items, Geners, Profile, Category
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .utils import recommend_similar_movies
import random

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {
        'profile': profile
    })

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, new_slug=slug)
    categories = Category.objects.all()
    side_items = Movie.objects.all()

    # Get top 20 movies by views (or change to rating if you prefer)
    top_movies = Movie.objects.exclude(id=movie.id).order_by('-views_count')[:20]

     # Randomly select 6 from the top movies
    recommended_movies = random.sample(list(top_movies), min(6, len(top_movies)))

    context = {
        'movie': movie,
        'categories': categories,
        'side_items': side_items,
        'recommended': recommended_movies,  # ← add this line
    }
    return render(request, 'core/movie_detail.html', context)


def home(request):
    banners = Banner.objects.all()
    most_popular = Movie.objects.order_by('-views_count')[:6]
    most_popular_ids = most_popular.values_list('id', flat=True)
    trending_now = Movie.objects.exclude(id__in=most_popular_ids).order_by('-release_date')[:6]
    top_rated = Movie.objects.order_by('-rating')[:6]
    side_items = Movie.objects.order_by('-views_count')[:5]

    # Recommended logic: get top 20 by views, randomly pick 6
    
    top_movies = Movie.objects.order_by('-views_count')[:20]
    recommended = random.sample(list(top_movies), min(6, len(top_movies)))

    context ={
        'most_popular': most_popular,
        'trending_now': trending_now,
        'banners': banners, 
        'side_items': side_items,
        'top_rated': top_rated,
        'recommended': recommended,
    }
    return render(request, 'index.html', context)



def movie_detail(request, slug):
    movie = Movie.objects.get(new_slug=slug)
    side_items = Side_items.objects.all()
    context ={
        'movie': movie,
        'side_items': side_items,
    }
    return render(request, 'anime-details.html', context)



def anime_watching(request, slug):
    movie = Movie.objects.get(new_slug=slug)

    context = {
        'movie':movie
    }
    return render(request, 'anime-watching.html', context)


def blog(request):
    return render(request, 'blog.html')


def categories(request, slug):
    categorie = slug
    genre = Geners.objects.get(title=slug)  # Assuming 'slug' is the title of the genre
    movies = Movie.objects.filter(genres=genre)
    side_items = Side_items.objects.all()
    context = {'movies': movies, 'categorie':categorie, 'side_items': side_items}
    return render(request, 'categories.html', context)


def categorie(request):
    movies = Movie.objects.filter(category='CO')
    context = {'movies': movies}
    return render(request, 'categories.html', context)


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(request, email=email, password=password)
            login(request, user)
            redirect('home')
            

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        if email and password and name:
            user = User.objects.create_user(email, password=password, username=name)
            user.save()
            redirect('home')
    return render(request, 'signup.html')