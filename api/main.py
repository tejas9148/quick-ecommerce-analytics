from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {
        "message": "Quick Commerce Analytics API Running"
    }