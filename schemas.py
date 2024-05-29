from pydantic import BaseModel

class Products(BaseModel):
    
    name: str
    description: str
    at_sale: bool
    price: str
    inventory: int
    