# app/crud.py
from sqlalchemy.orm import Session
from . import models

def create_product(db: Session, name: str, description: str, price: float):
    db_product = models.Product(name=name, description=description, price=price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()
