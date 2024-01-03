import requests

api_key = '98c750a3dca904870cfd203ded9f7a99'  

# Function to fetch movie details by title


def get_movie_details(movie_title):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}'
    response = requests.get(url)
    data = response.json()
    if 'results' in data and data['results']:
        return data['results'][0]
    else:
        return None

# Function to recommend movies based on a given movie title


def recommend_movies(movie_title):
    movie = get_movie_details(movie_title)
    if movie:
        movie_id = movie['id']
        url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}'
        response = requests.get(url)
        data = response.json()
        if 'results' in data:
            # Get the top 5 recommended movies
            recommended_movies = data['results'][:5]
            return recommended_movies
    return None

# AI component: Content-Based Filtering


def content_based_recommendations(movie_description, num_recommendations=5):
    # Analyze movie descriptions using AI techniques (e.g., TF-IDF)
    # Implement AI-based logic here to find movies with similar descriptions
    # For simplicity, we'll use the first num_recommendations from the API-based recommendations
    recommended_movies = recommend_movies(movie_description)
    return recommended_movies[:num_recommendations]


# Example usage
user_movie_title = input("Enter Movie Name: ")  # Input the movie title
recommended_movies = content_based_recommendations(user_movie_title)

if recommended_movies:
    print(f"Recommended Movies for '{user_movie_title}':")
    for movie in recommended_movies:
        print(movie['title'])
else:
    print(f"No recommendations found for '{user_movie_title}'.")
