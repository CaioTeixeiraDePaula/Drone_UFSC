from fastapi import FastAPI, APIRouter

app = FastAPI(debug=True)

img_router = APIRouter(prefix="/image/")