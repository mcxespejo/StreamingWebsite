from .models import Movie

def recommend_similar_movies(movie, limit=5):
    # Get all genre IDs for the selected movie
    movie_genres = movie.genres.values_list('id', flat=True)
    
    # Filter movies that share at least one genre and are not the movie itself
    recommended = (
        Movie.objects.filter(genres__in=movie_genres)
        .exclude(id=movie.id)
        .distinct()
        .order_by('-rating', '-views_count')[:limit]
    )
    return recommended
