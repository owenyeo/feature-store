from fastapi import FastAPI

app = FastAPI()

@app.get("user_features/{user_id}")
async def get_user(user_id):
    