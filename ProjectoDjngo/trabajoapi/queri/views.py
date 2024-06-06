import requests
from django.shortcuts import render

def movies_view(request):
    api_key = 'b28ab309'  
    url = f'http://www.omdbapi.com/?apikey={api_key}&s=star wars'  

    response = requests.get(url)
    data = response.json()

    movies = data.get('Search', [])  

    return render(request, 'movies.html', {'movies': movies})
