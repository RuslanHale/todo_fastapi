from fastapi import APIRouter
from todo import todo_router

router = APIRouter()


@router.get("/hello")
async def say_hello() -> dict:
    return { "message": "Hello!" }

