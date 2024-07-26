from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from transformers import pipeline

# Create a new FastAPI app instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")

# Define a root path to verify the server is running
@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")

# Define a function to handle the GET request at `/generate`
@app.get("/generate")
def generate(text: str):
    """
    Using the text2text-generation pipeline from `transformers`, generate text
    from the given input text. The model used is `google/flan-t5-small`.
    """
    # Use the pipeline to generate text from the given input text
    output = pipe(text)
    
    # Return the generated text in a JSON response
    return {"output": output[0]["generated_text"]}
