from fastapi import Query, status, HTTPException, Request, Depends, APIRouter
from fastapi.responses import HTMLResponse
from models import user as models
from schemas import user as schemas
from sqlalchemy.orm import Session
from dependencies import get_db
from dependencies import templates

router = APIRouter()


# render template
@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    PERSONS = [
        {"name": "salar", "age": 23, "height": 1.78},
        {"name": "ali", "age": 14, "height": 1.88},
        {"name": "hasan", "age": 45, "height": 1.68},
        {"name": "zara", "age": 22, "height": 1.77},
    ]
    return templates.TemplateResponse(
        request=request, name="index.html", context={"users": PERSONS}
    )


# path parameters
@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# query parameters
@router.get("/person/list")
async def persons_list(sort: str = Query(choices=["name", "age"])):
    return f"sort: {sort}"


@router.post("/user/add", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
async def create_person(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="username already exists!")
    new_user = models.User(username=user.username, password=user.password, created_time=user.created_time)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK, response_model=schemas.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="username not found!")
    return db_user
