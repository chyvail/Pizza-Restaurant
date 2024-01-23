# Flask Code Challenge - Pizza Restaurants

This project encompasses a robust backend with defined models, routes, and relationships centered around a Pizza Restaurant domain. The backend, constructed in Flask, provides a comprehensive API to interact with the underlying data.

# Backend API Link on Render

The link is available [here](https://pizza-restaurant-jl0u.onrender.com)

## Setup

To download the dependencies for the frontend and backend, run:

```sh
pipenv install
npm install --prefix client
```

There is some starter code in the `app/seed.py` file so that once you've
generated the models, you'll be able to create data to test your application.

You can run your Flask API on [`localhost:5555`](http://localhost:5555) by running:

```sh
python backend.py
```

You can run your React app on [`localhost:4000`](http://localhost:4000) by running:

```sh
npm start --prefix client
```

## Models

The project includes the following models and their relationships:

- A `Restaurant` model, which has many Pizzas through the `RestaurantPizza` model.
- A `Pizza` model, which has many Restaurants through the `RestaurantPizza` model.
- A `RestaurantPizza` model, representing the association between a `Restaurant` and a `Pizza`. This model includes a validation that enforces a price between 1 and 30.

## Run the migrations and seed file

```sh
flask db upgrade
python backend/seed.py
```

## Routes

The API exposes several routes to interact with the data. Each route returns JSON data in the specified format.

### GET /restaurants

Retrieves a list of restaurants:

```json
[
  {
    "id": 1,
    "name": "Sottocasa NYC",
    "address": "298 Atlantic Ave, Brooklyn, NY 11201"
  },
  {
    "id": 2,
    "name": "PizzArte",
    "address": "69 W 55th St, New York, NY 10019"
  }
]
```

### GET /restaurants/:id

Retrieve details about a specific restaurant by ID:

```json
{
  "id": 1,
  "name": "Sottocasa NYC",
  "address": "298 Atlantic Ave, Brooklyn, NY 11201",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}

```

If the `Restaurant` does not exist, return the following JSON data, along with
the appropriate HTTP status code:

```json
{
  "error": "Restaurant not found"
}
```

### GET /pizzas

Retrieves a list of pizzas:

```json
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```

### POST /restaurant_pizzas

Creates a new RestaurantPizza associated with an existing Pizza and Restaurant:

```json
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}

```

To access the routes and interact with the backend, use the appropriate HTTP verbs (GET, DELETE, POST) along with the specified endpoints.
