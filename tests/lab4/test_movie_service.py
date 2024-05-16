import unittest
from unittest.mock import patch
from src.lab4.movie_recommendation.models.movie_service import MovieService
from src.lab4.movie_recommendation.models.movie import Movie
from src.lab4.movie_recommendation.models.user import User

class TestMovieService(unittest.TestCase):
    def setUp(self):
        self.movies = {
            1: Movie(1, "Мстители: Финал"),
            2: Movie(2, "Хатико"),
            3: Movie(3, "Дюна"),
            4: Movie(4, "Унесенные призраками")
        }

        self.users = {
            "user1": User("user1", [1, 2, 3]),
            "user2": User("user2", [2, 3, 4])
        }

        with patch.object(MovieService, 'load_movies'), patch.object(MovieService, 'load_user_histories'):
            self.movie_service = MovieService('movies.json', 'user_histories.json')
            self.movie_service.movies = self.movies
            self.movie_service.users = self.users

    def test_recommend_movie_by_username_not_found(self):
        result = self.movie_service.recommend_movie_by_username("user3")
        self.assertEqual(result, "User not found")

    def test_recommend_movie_by_username(self):
        result = self.movie_service.recommend_movie_by_username("user1")
        self.assertEqual(result, "Унесенные призраками")

if __name__ == '__main__':
    unittest.main()