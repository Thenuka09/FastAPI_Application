
# pip install fastapi uvicorn

# 1. Library Import 
import uvicorn
from fastapi import FastAPI

# 2. Create the app object 
app = FastAPI()

# 3. Index route, opens automatically on https:// 127.0.0.1:8000
@app.get('/')
def index():
    return {'Message' : 'Hello, world'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to my API' : f'{name}'}

# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn main:app --reload




