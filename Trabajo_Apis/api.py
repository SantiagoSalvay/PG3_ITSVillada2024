import requests

API_KEY = '50a35843'

def requisito(endpoint, params={}):
    url = f'http://www.omdbapi.com/{endpoint}'
    params['apikey'] = API_KEY
    response = requests.get(url, params=params)
    return response.json()

def Pelicula():
    response = requisito('', params={'s': 'star wars', 'type': 'movie'})  
    return response['Search']

def Carta_Peliculas(movie):
    imdb_id = movie.get('imdbID', '')
    movie_details = requisito('', params={'i': imdb_id})
    
    title = movie_details.get('Title', '')
    year = movie_details.get('Year', '')
    director = movie_details.get('Director', '')
    actors = movie_details.get('Actors', '')
    released = movie_details.get('Released', '')
    writer = movie_details.get('Writer', '')
    imdb_rating = movie_details.get('imdbRating', '')
    poster = movie_details.get('Poster', '')

    card = f"""
        <div class="movie-card">
            <h2>{title} ({year})</h2>
            <p><strong>Director:</strong> {director}</p>
            <p><strong>Actores:</strong> {actors}</p>
            <p><strong>Lanzamiento:</strong> {released}</p>
            <p><strong>Escritor:</strong> {writer}</p>
            <p><strong>Calificación IMDb:</strong> {imdb_rating}</p>
            <img src="{poster}" alt="{title} Poster">
        </div>
    """
    return card

def HTML(movies):
    cards = ''.join([Carta_Peliculas(movie) for movie in movies])
    webpage_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resultados de la búsqueda</title>
        <style>
            .movie-card {{
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 20px;
                margin: 10px;
                width: 300px;
                float: left;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            }}
            h2 {{
                margin-bottom: 10px;
            }}
            img {{
                max-width: 100%;
                height: auto;
                display: block;
                margin: auto;
            }}
        </style>
    </head>
    <body>
        <h1>Resultados de la búsqueda</h1>
        {cards}
    </body>
    </html>
    """
    with open('resultados.html', 'w') as file:
        file.write(webpage_content)

if __name__ == "__main__":
    movies = Pelicula()
    HTML(movies)
    print("Se ha generado el archivo 'resultados.html' con las tarjetas de películas.")
