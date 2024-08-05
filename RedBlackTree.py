import csv
from datetime import datetime


class Node:
    def __init__(self, key, data, color='red'):
        self.key = key
        self.data = data
        self.color = color  # Nodes are initially inserted as red
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self, size=20):
        self.size = size
        self.NIL = Node(None, None, color='black')
        self.root = self.NIL

    def insert(self, key, data):
        new_node = Node(key, data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        self._insert_node(new_node)

    def _insert_node(self, new_node):
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.color = 'red'
        self._insert_fixup(new_node)

    def _insert_fixup(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'black'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, key):
        current = self.root
        while current != self.NIL:
            if key == current.key:
                return current.data
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, key):
        node_to_delete = self._search_node(self.root, key)
        if node_to_delete == self.NIL:
            return
        original_color = node_to_delete.color
        if node_to_delete.left == self.NIL:
            x = node_to_delete.right
            self._transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL:
            x = node_to_delete.left
            self._transplant(node_to_delete, node_to_delete.left)
        else:
            y = self._minimum(node_to_delete.right)
            original_color = y.color
            x = y.right
            if y.parent == node_to_delete:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y
            self._transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.color = node_to_delete.color
        if original_color == 'black':
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _search_node(self, node, key):
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def read_csv_and_insert_into_tree(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                if count >= self.size:
                    break
                title = row['title']
                data = {
                    'vote_average': row['vote_average'],
                    'vote_count': row['vote_count'],
                    'release_date': row['release_date'],
                    'revenue': row['revenue'],
                    'runtime': row['runtime'],
                    'backdrop_path': row['backdrop_path'],
                    'budget': row['budget'],
                    'homepage': row['homepage'],
                    'imdb_id': row['imdb_id'],
                    'original_language': row['original_language'],
                    'overview': row['overview'],
                    'popularity': row['popularity'],
                    'poster_path': row['poster_path'],
                    'tagline': row['tagline'],
                    'genres': row['genres'],
                    'production_companies': row['production_companies'],
                    'production_countries': row['production_countries'],
                    'spoken_languages': row['spoken_languages'],
                    'keywords': row['keywords']
                }
                self.insert(title, data)
                count += 1

    def filter(self, filters_with_priorities):
        # Start with all movies
        results = []
        self._inorder_traversal(self.root, results)

        # Apply each filter in the order of priority
        for filter_name, filter_value in filters_with_priorities:
            if filter_name == 'vote_average':
                results = [
                    (title, data) for title, data in results
                    if filter_value[0] <= float(data['vote_average']) <= filter_value[1]
                ]
            elif filter_name == 'popularity':
                results = [
                    (title, data) for title, data in results
                    if filter_value[0] <= float(data['popularity']) <= filter_value[1]
                ]
            elif filter_name == 'revenue':
                results = [
                    (title, data) for title, data in results
                    if (filter_value[0] * 1000000000) <= float(data['revenue']) <= (filter_value[1] * 1000000000)
                ]
            elif filter_name == 'runtime':
                results = [
                    (title, data) for title, data in results
                    if filter_value[0] <= float(data['runtime']) <= filter_value[1]
                ]
            elif filter_name == 'genres' and len(filter_value) > 0:
                results = [
                    (title, data) for title, data in results
                    if filter_value[0].lower() in data['genres'].lower()
                ]
            elif filter_name == 'keywords' and filter_value is not None:
                filter_keywords = [kw.strip().lower() for kw in filter_value.split(',')]
                results = [
                    (title, data) for title, data in results
                    if any(kw in data['keywords'].lower() for kw in filter_keywords)
                ]
            elif filter_name == 'production_countries' and len(filter_value) > 0:
                results = [
                    (title, data) for title, data in results
                    if filter_value[0].lower() in data['production_countries'].lower()
                ]
            elif filter_name == 'original_language' and filter_value is not None:
                results = [
                    (title, data) for title, data in results
                    if filter_value[:2].lower() == data['original_language'].lower()
                ]
            elif filter_name == "release_date":
                start_year = int(filter_value[0])
                end_year = int(filter_value[1])
                results = [
                    (title, data) for title, data in results
                    if 'release_date' in data and data['release_date']
                       and start_year <= datetime.strptime(data['release_date'], '%Y-%m-%d').year <= end_year
                ]

        return results

    def _inorder_traversal(self, node, results):
        if node != self.NIL:
            self._inorder_traversal(node.left, results)
            results.append((node.key, node.data))
            self._inorder_traversal(node.right, results)
