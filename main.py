# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, database

# Veritabanı başlatma
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Veritabanı bağlantısı
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ürün ekleme
@app.post("/products/")
def create_product(name: str, description: str, price: float, db: Session = Depends(get_db)):
    return crud.create_product(db=db, name=name, description=description, price=price)

# Ürünleri listeleme
@app.get("/products/")
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db=db, skip=skip, limit=limit)
