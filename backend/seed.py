from backend import db, app
from models import Restaurant, Pizza, RestaurantPizza

with app.app_context():

    # Seed data for Restaurant model
    restaurants_data = [
        {"name": "Sottocasa NYC", "address": "298 Atlantic Ave, Brooklyn, NY 11201"},
        {"name": "PizzArte", "address": "69 W 55th St, New York, NY 10019"},
        {"name": "Joe's Pizzeria", "address": "123 Main St, Anytown, USA"},
        {"name": "Slice Heaven", "address": "456 Oak St, Cityville, USA"},
        {"name": "Mama Mia's", "address": "789 Elm St, Townsville, USA"},
        {"name": "Peppy's Pizza", "address": "101 Pine St, Villageland, USA"},
        {"name": "Cheesy Delight", "address": "202 Maple St, Hamletown, USA"},
        {"name": "Gourmet Pies", "address": "303 Birch St, Suburbia, USA"},
        {"name": "Urban Crust", "address": "404 Cedar St, Metropolis, USA"},
        {"name": "Tasty Bites", "address": "505 Spruce St, Riverside, USA"},
    ]

    for data in restaurants_data:
        restaurant = Restaurant(**data)
        db.session.add(restaurant)

    # Seed data for Pizza model
    pizzas_data = [
        {"name": "Margherita", "ingredients": "Tomato Sauce, Mozzarella, Basil"},
        {"name": "Pepperoni", "ingredients": "Tomato Sauce, Mozzarella, Pepperoni"},
        {"name": "Vegetarian", "ingredients": "Tomato Sauce, Mozzarella, Vegetables"},
        {"name": "BBQ Chicken", "ingredients": "BBQ Sauce, Chicken, Red Onions"},
        {"name": "Hawaiian", "ingredients": "Tomato Sauce, Mozzarella, Ham, Pineapple"},
        {"name": "Meat Lovers", "ingredients": "Tomato Sauce, Mozzarella, Sausage, Bacon, Pepperoni"},
        {"name": "Spinach and Feta", "ingredients": "Tomato Sauce, Mozzarella, Spinach, Feta"},
        {"name": "Buffalo Chicken", "ingredients": "Buffalo Sauce, Chicken, Blue Cheese"},
        {"name": "Seafood Delight", "ingredients": "Tomato Sauce, Mozzarella, Shrimp, Clams, Garlic"},
        {"name": "Mushroom Madness", "ingredients": "Tomato Sauce, Mozzarella, Mushrooms, Onions"},
    ]

    for data in pizzas_data:
        pizza = Pizza(**data)
        db.session.add(pizza)

    # Seed data for RestaurantPizza model
    restaurant_pizzas_data = [
        {"restaurant_id": 1, "pizza_id": 1, "price": 12.99},
        {"restaurant_id": 1, "pizza_id": 2, "price": 14.99},
        {"restaurant_id": 2, "pizza_id": 3, "price": 13.99},
        {"restaurant_id": 2, "pizza_id": 4, "price": 15.99},
        {"restaurant_id": 3, "pizza_id": 5, "price": 16.99},
        {"restaurant_id": 3, "pizza_id": 6, "price": 17.99},
        {"restaurant_id": 4, "pizza_id": 7, "price": 18.99},
        {"restaurant_id": 4, "pizza_id": 8, "price": 19.99},
        {"restaurant_id": 5, "pizza_id": 9, "price": 20.99},
        {"restaurant_id": 5, "pizza_id": 10, "price": 21.99},
    ]

    for data in restaurant_pizzas_data:
        restaurant_pizza = RestaurantPizza(**data)
        db.session.add(restaurant_pizza)

    # Commit changes to the database
    db.session.commit()

    print("🦸‍♀️ Done seeding!")
