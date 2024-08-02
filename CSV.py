import csv
class Movie:
    def __init__(self, title, rating, runtime, genre, metascoreStr, plot, director, stars, votesStr, grossStr, link):
        self.title = title
        self.rating = float(rating)
        self.runtime = int(runtime.split()[0]) if 'min' in runtime else 0
        self.genre = genre
        self.metascore = int(metascoreStr) if metascoreStr else 0
        self.plot = plot
        self.director = director
        self.stars = stars
        self.votes = int(votesStr) if votesStr else 0
        try:
            self.gross = int(grossStr.replace(',', ''))
        except ValueError:
            self.gross = 0
        self.link = link
        self.vecGenres = [g.strip() for g in genre.split(',')]
    def __str__(self):
        return f'Title: {self.title}\nRating: {self.rating}\nRuntime: {self.runtime}\nGenre: {self.genre}\nMetascore: {self.metascore}\nPlot: {self.plot}\nDirector: {self.director}\nStars: {self.stars}\nVotes: {self.votes}\nGross: {self.gross}\nLink: {self.link}\n'
class CSVReader:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # Skip header

            self.Movies = [Movie(*row) for row in csv_reader]
    def printMovies(self):
        for movie in self.Movies:
            print(str(movie))
            print("------------------------")
# Usage
reader = CSVReader('CSV.csv')
reader.printMovies()
