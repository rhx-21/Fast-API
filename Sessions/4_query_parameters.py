# Use in filtering, sorting, searching 
# e.g.  /product?price=500

from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def user(name: str = None):         # optional parameter
    return {
    "Name": name
}
    
@app.get("/products")
def product(limit: int = 5):        # default value
    return{
        "Limit": limit
    }
    
@app.get("/items")
def items(name: str = None, price: int = 0):     # multiple query parameters
    return{
        "Name": name,
        "Price": price
    }
