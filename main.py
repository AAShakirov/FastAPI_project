from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router
from schemas import STaskAdd

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('DROP')
    await create_tables()
    print('Base is ready')
    yield
    print('OFF')


app = FastAPI(lifespan=lifespan)
app.include_router(router=tasks_router)

@app.get('/')
async def get_file_text():
    return {'ok': True}
