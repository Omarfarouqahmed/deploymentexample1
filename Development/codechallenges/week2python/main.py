from customer import Customer
from restaurant import Restaurant

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
        

for restaurant in Restaurant.all_restaurants:
    print(f"{restaurant.name}")