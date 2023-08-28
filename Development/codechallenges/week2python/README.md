# Object Relations Code Challenge - Restaurants
For this assignment, we'll be working with a Yelp-style domain.
 We have three models:
- `Restaurant`
- `Customer`
- `Review`
 For our purposes, a `Restaurant` has many `Reviews`, a `Customer` has many `Review`s, and a `Review` belongs to a `Customer` and to a `Restaurant`.
 `Restaurant` - `Customer` is a many-to-many relationship.
 
Topics
- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

### breakdown of the challenge
Initializers, Readers, and Writers
#### Customer
- `Customer __init__()`
  - Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
- `Customer given_name()`
  - returns the customer's given name
  - `Customer family_name()`
  - returns the customer's family name
  - `Customer full_name()`
  - returns the full name of the customer, with the given name and the family name concatenated.
- `Customer all()`
  - returns **all** of the customer instances

#### Restaurant
- `Restaurant __init__()`
  - Restaurants should be initialized with a name, as a string
- `Restaurant name()`
  - returns the restaurant's name
  
 #### Review
- `Review __init__()`
  - Reviews should be initialized with a customer, restaurant, and a rating (a number)
- `Review rating()`
  - returns the rating for a restaurant.
- `Review all()`
  - returns all of the reviews
Object Relationship Methods
Review
- `Review customer()`
  - returns the customer object for that review
  - Once a review is created, should not be able to change the customer
- `Review restaurant()`
  - returns the restaurant object for that given review
  - Once a review is created, should not be able to change the restaurant
Restaurant
- `Restaurant reviews()`
  - returns a list of all reviews for that restaurant
- `Restaurant customers()`
  - Returns a **unique** list of all customers who have reviewed a particular restaurant.
Customer
- `Customer restaurants()`
  - Returns a **unique** list of all restaurants a customer has reviewed
- `Customer add_review(restaurant, rating)`
  - given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.

## License
This challenge is licensed under the MIT License.
