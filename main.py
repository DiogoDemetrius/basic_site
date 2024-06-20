from fastapi import FastAPI, Depends, HTTPException, Request, status, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic import BaseModel
from auth import get_db, authenticate_user, get_password_hash
import models
from database import SessionLocal, engine, Base

# Criação das tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Pydantic model for user registration
class UserCreate(BaseModel):
    username: str
    password: str

# Pydantic model for car registration
class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    price: float

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    cars = db.query(models.Car).all()
    return templates.TemplateResponse("index.html", {"request": request, "cars": cars})

@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
def login_user(request: Request, db: Session = Depends(get_db), username: str = Form(...), password: str = Form(...)):
    user = authenticate_user(db, username, password)
    if not user:
        message = "Credenciais inválidas!"
        return templates.TemplateResponse("login.html", {"request": request, "message": message})
    message = f"Bem-vindo! {username}"
    return templates.TemplateResponse("index.html", {"request": request, "cars": db.query(models.Car).all(), "message": message})

@app.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
def create_user(request: Request, db: Session = Depends(get_db), username: str = Form(...), password: str = Form(...)):
    hashed_password = get_password_hash(password)
    db_user = models.User(username=username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/cars/register", response_class=HTMLResponse)
def register_car_form(request: Request):
    return templates.TemplateResponse("car_register.html", {"request": request})

@app.post("/cars/register", response_class=HTMLResponse)
def register_car(request: Request, db: Session = Depends(get_db), make: str = Form(...), model: str = Form(...), year: int = Form(...), price: float = Form(...)):
    db_car = models.Car(make=make, model=model, year=year, price=price)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return templates.TemplateResponse("index.html", {"request": request, "cars": db.query(models.Car).all()})

@app.get("/cars/{car_id}", response_class=HTMLResponse)
def car_detail(car_id: int, request: Request, db: Session = Depends(get_db)):
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return templates.TemplateResponse("car_detail.html", {"request": request, "car": car})

@app.get("/cars", response_class=HTMLResponse)
def list_cars(request: Request, db: Session = Depends(get_db)):
    cars = db.query(models.Car).all()
    return templates.TemplateResponse("cars.html", {"request": request, "cars": cars})
