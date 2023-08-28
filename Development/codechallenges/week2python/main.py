from customer import Customer
from restaurant import Restaurant

# making test cases
c1 = Customer("Omar", "Ali")
c2 = Customer("Will", "Smith")

r1 = Restaurant("Drip Burger")
r2 = Restaurant("Pizza Hut")

c1.add_review(r1, 4)
c2.add_review(r1, 5)
c2.add_review(r2, 3)


# print("Customers:")
# for customer in Customer.all_customers:
#     print(customer.full_name())


print("Restaurant Reviews:")
for restaurant in Restaurant.all_restaurants:
    print(f"{restaurant.name} Reviews:")
    for review in restaurant.reviews:
        customer_name = review.customer.full_name()
        rating = review.rating
        print(f"  - {customer_name}: {rating}")