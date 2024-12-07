from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("DATABASE_URL")
DB_URL = "sqlite:///./database.db" if url is None else url
PROJECT_DIR = Path(__file__).resolve().parent.parent
