import os
from dotenv import load_dotenv  # Only needed if using .env file
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file (if used)
load_dotenv()

# Get the API key from the environment variable
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Check if the API key is available
if not GEMINI_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.  Please set it.")

# Initialize the Gemini model
llm = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

# Define a prompt template
prompt_template = ChatPromptTemplate.from_template("What is the capital of {country}?")

# Create an LLMChain
chain = prompt_template | llm

# Run the chain
capital = chain.invoke("France")

# Print the result
print(f"The capital of France is: {capital}")


country = "Japan"
capital = chain.invoke("Japan")

# Print the result
print(f"The capital of {country} is: {capital}")

