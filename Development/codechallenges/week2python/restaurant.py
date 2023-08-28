class Restaurant:
    all_restaurants = []
# initializing class
    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)
# identifying methods
    def add_review(self, review):
        self.reviews.append(review)

    def reviews(self):
        return self.reviews

    def customers(self):
        return list({review.customer for review in self.reviews})

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating for review in self.reviews)
        return total_ratings / len(self.reviews)



