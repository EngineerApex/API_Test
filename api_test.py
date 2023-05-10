from fastapi import FastAPI, File, UploadFile
from typing import List
from io import BytesIO
from PIL import Image

app = FastAPI()

def api_test():
    output = "thisiss"
    return output

@app.get("/")
async def root():
    return {"message": api_test()}

if __name__ == "__main__":
    import uvicorn
    # Run the app using Uvicorn server
    uvicorn.run("api_test:app", host="127.0.0.1", port=8000, reload=True)