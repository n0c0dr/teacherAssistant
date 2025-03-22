from pydantic_settings import BaseSettings
from pathlib import Path
from typing import Optional
import os
from dotenv import load_dotenv 

class Settings(BaseSettings):
    # Model settings
    GEMINI_API_KEY:str = ""
    GEMINI_EMBEDDING_MODEL:str = ""

    # File storage settings

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    STORAGE: Path = os.path.join(BASE_DIR , "storage")
    UPLOAD_DIR: Path = os.path.join(STORAGE , "uploads")
    OUTPUT_DIR: Path = os.path.join(STORAGE , "outputs")
    STATIC_DIR: Path = os.path.join(STORAGE , "static")
    SOURCE_DIR: Path = os.path.join(STORAGE , "source_documnet")
    VECTOR_DB_DIR: Path = os.path.join(STORAGE , "vector_db")

    # constructor 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.GEMINI_API_KEY:str = os.environ["GEMINI_API_KEY"]
        if self.GEMINI_API_KEY == "":
            raise ValueError("GEMINI_API_KEY not found in environment variables.  Please set it.")
        #  create necessary directories
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        self.STATIC_DIR.mkdir(parents=True, exist_ok=True)
        self.SOURCE_DIR.mkdir(parents=True, exist_ok=True)
        self.VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)
        print("Settings loaded")
    

setting = Settings()
