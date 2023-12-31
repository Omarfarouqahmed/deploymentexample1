from customer import Customer
from restaurant import Restaurant
from review import Review

# making test cases
customer1 = Customer("Omar", "Ali")
customer2 = Customer("Will", "Smith")
customer3 = Customer ("Jumba", "Snr")

res1 = Restaurant("Drip Burger")
res2 = Restaurant("Pizza Hut")
res3 = Restaurant("Jaja")

customer1.add_review(res1, 4)
customer2.add_review(res1, 5)
customer2.add_review(res2, 3)
customer3.add_review(res3, 5)
customer1.add_review(res2, 4)
customer1.add_review(res3, 3)

# print("Customers:")
# for customer in Customer.all_customers:
#     print(customer.full_name())


# print("Restaurant Reviews:")
# for restaurant in Restaurant.all_restaurants:
#     print(f"{restaurant.name} Reviews:")
#     for review in restaurant.reviews:
#         customer_name = review.customer.full_name()
#         rating = review.rating
#         print(f"  - {customer_name}: {rating}")
        

# for restaurant in Restaurant.all_restaurants:
#     print(f"{restaurant.name}")

# print("Special List of Customers and Their Reviewed Restaurants:")
# for customer in Customer.all_customers:
#     reviewed_restaurants = ", ".join([review.restaurant.name for review in customer.reviews])
#     print(f"{customer.full_name()} reviewed: {reviewed_restaurants}")

print("Restaurants Reviewed by Customers with Ratings:")
for customer in Customer.all_customers:
    print(f"{customer.full_name()} reviewed:")
    for review in customer.reviews:
        print(f"- {review.restaurant.name} with a rating of {review.rating}")