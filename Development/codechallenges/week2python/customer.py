from restaurant import Restaurant
from review import Review

class Customer:
    all_customers = []
# initializing the class
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)
# identifying methods
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.add_review(review)


# Making test cases
# c1 = Customer("Omar", "Ahmed")
# c2 = Customer("Will", "Smith")

# r1 = Restaurant("Tasty Burger")
# r2 = Restaurant("Pizza Hut")

# c1.add_review(r1, 4)
# c2.add_review(r1, 5)
# c2.add_review(r2, 3)
