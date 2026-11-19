from fastapi import FastAPI

app = FastAPI()

@app.get('/blog/{slug}')
async def root(slug: int):
    return {'message': slug}



