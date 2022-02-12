from django.shortcuts import render
from watchlist_app.models import Movie
from django.shortcuts import render


# list of all movies
def movie_list(request):
    movies = Movie.objects.all()
    data = {'movies': list(movies.values())}
    return render(request, 'movie_list.html', {'data':data})


# details of individual movie
# details of individual movie
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active,
    }
    return render(request, 'movie_details.html', {'data': data})
    
