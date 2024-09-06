from fastapi import FastAPI
from .crud.board_crud import board_router
from .database import Base, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(board_router, prefix="/boards", tags=["boards"])

@app.get('/')
def get_home():
    return {'message': 'Home neagga'}


