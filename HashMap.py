import csv
from datetime import datetime


class HashMap:
    def __init__(self, size=20):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, data):
        index = self._hash(key)
        for i, entry in enumerate(self.table[index]):
            if entry[0] == key:
                self.table[index][i] = (key, data)
                return
        self.table[index].append((key, data))

    def search(self, key):
        index = self._hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, entry in enumerate(self.table[index]):
            if entry[0] == key:
                del self.table[index][i]
                return

    def print_hashmap(self):
        for index, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {index}:")
                for key, value in bucket:
                    print(f"  {key}: {value}")

    def read_csv_and_insert_into_hashmap(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                if count >= self.size:
                    break  # Stop reading if the limit is reached
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
        for bucket in self.table:
            for title, data in bucket:
                results.append((title, data))

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
                    if (filter_value[0]*1000000000) <= float(data['revenue']) <= (filter_value[1]*1000000000)
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
