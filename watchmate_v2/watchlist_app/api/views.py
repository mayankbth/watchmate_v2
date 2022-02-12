from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# list of all movies
def movie_list(request):
    movies = Movie.objects.all()
    data = {'movies': list(movies.values())}
    return JsonResponse(data)


# details of individual movie
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active,
    }
    return JsonResponse(data)