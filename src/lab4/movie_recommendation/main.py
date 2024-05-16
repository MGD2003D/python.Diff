from models.movie_service import MovieService

def main():
    movie_service = MovieService('data/movies.json', 'data/user_histories.json')
    username = input("Enter your username: ")

    recommendation = movie_service.recommend_movie_by_username(username)
    print(f"Recommended movie: {recommendation}")

if __name__ == "__main__":
    main()