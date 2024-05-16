import json
from .movie import Movie
from .user import User

class MovieService:
    def __init__(self, movies_file, history_file):
        self.movies = {}
        self.users = {}
        self.load_movies(movies_file)
        self.load_user_histories(history_file)

    def load_movies(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for movie_id, title in data.items():
                self.movies[int(movie_id)] = Movie(int(movie_id), title)

    def load_user_histories(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for username, movie_ids in data.items():
                self.users[username] = User(username, list(map(int, movie_ids)))

    def recommend_movie_by_username(self, username):
        if username not in self.users:
            return "User not found"

        user_movies_set = set(self.users[username].viewed_movies)
        half_len = len(user_movies_set) / 2
        recommendations = {}

        for user in self.users.values():
            if user.username != username:
                intersection_len = len(user_movies_set.intersection(set(user.viewed_movies)))
                if intersection_len >= half_len:
                    weight = intersection_len / len(user_movies_set)
                    for movie_id in user.viewed_movies:
                        if movie_id not in user_movies_set:
                            if movie_id not in recommendations:
                                recommendations[movie_id] = weight
                            else:
                                recommendations[movie_id] += weight

        if recommendations:
            recommended_movie_id = max(recommendations, key=recommendations.get)
            return self.movies[recommended_movie_id].title
        return "No recommendation available"