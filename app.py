from flask import Flask, render_template, request
import requests
import urllib.parse

app = Flask(__name__, template_folder='templates')

# Your movie recommendation functions here
api_key = '98c750a3dca904870cfd203ded9f7a99'

# Function to fetch movie details by title


def get_movie_details(movie_title):
    base_url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': api_key,
        'query': movie_title
    }
    url = f'{base_url}?{urllib.parse.urlencode(params)}'
    response = requests.get(url)
    data = response.json()
    if 'results' in data and data['results']:
        return data['results'][0]
    else:
        return None

# Function to recommend movies based on a given movie title
# (You can add your recommendation logic here)

# AI component: Content-Based Filtering
# (You can implement content-based filtering here)

# Define the content-based recommendation function


def content_based_recommendations(movie_title, num_recommendations=5):
    # Replace this with a call to your actual recommendation function or API
    recommended_movies = get_actual_recommendations(movie_title)
    return recommended_movies[:num_recommendations]

# Function to get actual movie recommendations based on movie title from an API


def get_actual_recommendations(movie_title):
    # Use the movie_title to fetch movie details
    movie = get_movie_details(movie_title)
    if movie:
        movie_id = movie.get('id')
        if movie_id:
            url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
            params = {'api_key': api_key}
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if 'results' in data:
                    return data['results']

    # Return an empty list if no recommendations are found or an error occurs
    return []


def get_movie_poster(movie_title):
    movie = get_movie_details(movie_title)
    if movie:
        poster_path = movie.get('poster_path')
        if poster_path:
            # You can choose the desired image size
            base_url = 'https://image.tmdb.org/t/p/w500'
            poster_url = f'{base_url}{poster_path}'
            return poster_url
    return None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_movie_title = request.form['movie_title']
        recommended_movies = content_based_recommendations(user_movie_title)
        return render_template('recommendations.html', user_movie_title=user_movie_title, recommended_movies=recommended_movies, get_movie_poster=get_movie_poster)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
