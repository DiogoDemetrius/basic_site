from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from auth import get_db, authenticate_user, get_password_hash
import models
from database import SessionLocal, engine, Base

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    cars = db.query(models.Car).all()
    return templates.TemplateResponse("index.html", {"request": request, "cars": cars})

@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
def login_user(username: str, password: str, request: Request, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return templates.TemplateResponse("index.html", {"request": request, "cars": db.query(models.Car).all()})

@app.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
def create_user(username: str, password: str, request: Request, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(password)
    db_user = models.User(username=username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/cars", response_class=HTMLResponse)
def list_cars(request: Request, db: Session = Depends(get_db)):
    cars = db.query(models.Car).all()
    return templates.TemplateResponse("cars.html", {"request": request, "cars": cars})

@app.get("/cars/{car_id}", response_class=HTMLResponse)
def car_detail(car_id: int, request: Request, db: Session = Depends(get_db)):
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return templates.TemplateResponse("car_detail.html", {"request": request, "car": car})
