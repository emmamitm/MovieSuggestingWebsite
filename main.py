from User import User, MoviesDB

if __name__ == '__main__':
    m = set()
    user1 = User("CSV.csv", "action", 10, 5, 120, 90, 0, "h", m, m)
    movie = MoviesDB(user1)
