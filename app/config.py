# config.py

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    APP_NAME = "Clinical Trial Management System"
    APP_VERSION = "1.0.0"

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost/clinical_trial_db"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "clinicaltrialsecretkey123"
    )

    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

settings = Settings()