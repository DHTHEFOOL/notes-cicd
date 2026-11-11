import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Đọc biến môi trường từ file .env (file này KHÔNG được commit lên GitHub)
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+psycopg://notes:notes@localhost:5432/notes"
)

engine = create_engine(
    DATABASE_URL, pool_pre_ping=True, connect_args={"connect_timeout": 3}
)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
