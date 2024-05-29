from fastapi import FastAPI, Depends, HTTPException, status
from . import models
from .database import engine
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import Products


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"Hello": "World"}


@app.post("/product")
async def create_product(product: Products, db: Session = Depends(get_db)):
    
    new_product = models.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.get("/product")
async def get_products(db: Session = Depends(get_db)):
    all_products = db.query(models.Product).all()
    return all_products


@app.delete("/product/{product_id}")
async def delete_product(product_id: str, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    else:
        db.delete(product)
        db.commit()
    return {"message": "Product deleted successfully"}


@app.put("/product/{product_id}")
async def update_product(product_id: str, product: Products, db: Session = Depends(get_db)):
    product_to_update = db.query(models.Product).filter(models.Product.id == product_id)
    product_to_update.first()
    if product_to_update is None:
        raise HTTPException(status_code=404, detail="Product not found")
    else:
        product_to_update.update(product.dict())
        db.commit()
    return product_to_update.first()
