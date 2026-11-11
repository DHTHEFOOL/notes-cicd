from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import text

from app.database import engine

app = FastAPI(title="Notes API", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Notes API is running"}


@app.get("/health")
def health():
    """Kiểm tra ứng dụng và kết nối cơ sở dữ liệu.

    Trả về 200 khi kết nối được PostgreSQL, 503 khi không kết nối được.
    Endpoint này sẽ được pipeline CD dùng để kiểm tra sau khi triển khai.
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception:
        return JSONResponse(
            status_code=503,
            content={"status": "error", "database": "disconnected"},
        )
