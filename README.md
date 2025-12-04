Background Removal API Deployment

How to deploy to Railway

GitHub Method (Recommended):

Create a new repository on GitHub.

Push the three files (main.py, requirements.txt, Procfile) to that repository.

Go to Railway.app.

Click "New Project" -> "Deploy from GitHub repo".

Select your repository.

Railway will automatically detect the Procfile and requirements.txt and start building.

Railway CLI Method:

Install the Railway CLI.

Run railway login.

Inside this folder, run railway init.

Run railway up.

Testing the API

Once deployed, Railway will give you a public URL (e.g., https://web-production-xxxx.up.railway.app).

You can test it using a tool like Postman or curl:

# Replace YOUR_RAILWAY_URL with the actual URL
curl -X POST -F "file=@/path/to/your/image.jpg" https://YOUR_RAILWAY_URL/remove-bg --output result.png


Note on First Run

The first time the API processes an image, rembg will download the U2NET machine learning model (approx 170MB). This might make the very first request take a few seconds longer than usual.