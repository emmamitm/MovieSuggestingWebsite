from CSV import CSVReader, Movie
class Node:
    def __init__(self, score, movie):
        self.score = score
        self.movie = movie
        self.height = 1
        self.left = None
        self.right = None

class User:
    def __init__(self, filename, genre, rating_high, rating_low, runtime_high, runtime_low,
                 meta_score, plot, watched_movies, tags):
        self.reader = CSVReader(filename)
        self.genre = genre
        self.rating_high = rating_high
        self.rating_low = rating_low
        self.runtime_high = runtime_high
        self.runtime_low = runtime_low
        self.meta_score = meta_score
        self.plot = plot
        self.watched_movies = set(watched_movies)
        self.tags = set(tags)

    def get_movies(self):
        return self.reader.Movies

    def add_watched_movie(self, movie):
        self.watched_movies.add(movie)

    def add_tag(self, tag):
        self.tags.add(tag)

class Node:
    def __init__(self, score, movie):
        self.score = score
        self.movie = movie
        self.height = 1
        self.left = None
        self.right = None


class MoviesDB:
    def __init__(self, user):
        self.user = user
        self.movies = user.get_movies()
        self.root = None
        self.number = 0
        self.initialize_binary_tree()
        #self.titles = []
        #self.print_inorder(self.root, self.titles)
        self.print_best_order(self.root)

    def initialize_binary_tree(self):
        for i, movie in enumerate(self.movies):
            #number = self.score_calculator(movie)
            number =i
            self.insert(number, movie)

    def score_calculator(self, movie):
        rating_portion = ((self.user.rating_high - self.user.rating_low) -
                          min(self.user.rating_high - movie.rating,
                              movie.rating - self.user.rating_low)) / (
                                 self.user.rating_high - self.user.rating_low)
        runtime_portion = ((self.user.runtime_high - self.user.runtime_low) -
                           min(self.user.runtime_high - movie.rating,
                               movie.rating - self.user.runtime_low)) / (
                                  self.user.runtime_high - self.user.runtime_low)
        genre_portion = 1 if self.user.genre in movie.genre else 0
        score = 0.25 * (rating_portion +
                        runtime_portion +
                        genre_portion +
                        1.0)
        return score

    def insert(self, score, movie):
        if not self.root:
            self.root = Node(score, movie)
        else:
            self.root = self.insert_helper(self.root, score, movie)

    def insert_helper(self, node, score, movie):
        if node is None:
            node = Node(score, movie)
        elif score < node.score:
            node.left = self.insert_helper(node.left, score, movie)
        elif score > node.score:
            node.right = self.insert_helper(node.right, score, movie)
        else:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Left tree is heavy
        if self.get_balance(node) > 1:
            # Left right case
            if score > node.left.score:
                node.left = self.rotate_left(node.left)
            # Left left case
            node = self.rotate_right(node)
        elif self.get_balance(node) < -1:
            # Right left case
            if score < node.right.score:
                node.right = self.rotate_right(node.right)
            # Right right case
            node = self.rotate_left(node)

        return node

    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.height = max(self.height(root.left), self.height(root.right)) + 1
        new_root.height = max(self.height(new_root.left), self.height(new_root.right)) + 1
        return new_root

    def rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.height = max(self.height(root.left), self.height(root.right)) + 1
        new_root.height = max(self.height(new_root.left), self.height(new_root.right)) + 1
        return new_root

    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def height(self, node):
        if not node:
            return 0
        return node.height
    def print_best_order(self, node):
        if node:
            self.print_best_order(node.right)
            print(node.movie.title, end=", ")
            self.print_best_order(node.left)
    def count_nodes(self, node):
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right) if node else 0

    def print_inorder(self, node, titles):
        if node:
            self.print_inorder(node.left, titles)
            titles.append(node.movie.title)
            self.print_inorder(node.right, titles)



