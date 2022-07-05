from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# CORS necessary for talking to other domains


from . import models
from .database import engine
from .routers import post, user, auth, vote

# https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-joins/
# select posts.*, COUNT(vote.post_id) as votes from posts LEFT JOIN vote on posts.id = vote.post_id group by posts.id;

# don't need salch to make tables since is handled by alembic
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# list of origins that can access our API
origins = ["https://www.google.com"]

# Middle ware is function that runs  function before every  request
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")  # uvicorn app.main:app --reload
def root():
    return {"message": "Hello World"}


# prod start:
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
