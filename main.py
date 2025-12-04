from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response
from rembg import remove
import io
from PIL import Image

app = FastAPI(title="Background Remover API")

@app.get("/")
def read_root():
    return {"message": "Background Removal API is running. POST images to /remove-bg"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    """
    Accepts an image file, removes the background, and returns the PNG.
    """
    try:
        # Read the image file into memory
        input_image = await file.read()
        
        # Validate that it is actually an image (basic check)
        if not input_image:
            raise HTTPException(status_code=400, detail="Empty file sent")

        # Process the image using rembg
        # rembg.remove() accepts bytes and returns bytes (PNG with alpha channel)
        output_image = remove(input_image)

        # Return the result as a PNG image
        return Response(content=output_image, media_type="image/png")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # This block allows running locally with `python main.py`
    uvicorn.run(app, host="0.0.0.0", port=8000)