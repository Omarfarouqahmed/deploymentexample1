class Review:
    all_reviews = []
# initializing class 
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
# identifying methods
    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant
# class method
    @classmethod
    def all(cls):
        return cls.all_reviews



