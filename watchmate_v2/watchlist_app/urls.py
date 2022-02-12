from django.urls import path, include
from watchlist_app.views import movie_list, movie_details


urlpatterns = [
    # REST api
    path('api/', include('watchlist_app.api.urls')),
    
    # django    
    path('list/', movie_list, name='movie-list'),
    path('<int:pk>/', movie_details, name='movie-details'),
]
