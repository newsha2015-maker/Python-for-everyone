"""
Assignment 5: FastAPI (Optional)

*If you have FastAPI and Uvicorn installed (`pip install fastapi uvicorn`), you can attempt this assignment.*

1.  Create a new FastAPI application.
2.  Create a Pydantic model for a `Product` with the following fields: `name` (string), `price` (float), and `is_in_stock` (boolean).
3.  Create a POST endpoint `/products` that accepts a `Product` object and returns it.
4.  Create a GET endpoint `/products` that returns a list of `Product` objects (you can hardcode a list for now).
5.  Run the application with Uvicorn and test your endpoints using the automatically generated docs at `/docs`.
"""
