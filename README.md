# Notes CI/CD

Đề tài Project 1: Xây dựng hệ thống CI/CD tự động, bảo mật và có đo đạc hiệu năng cho ứng dụng REST API quản lý ghi chú (FastAPI + PostgreSQL).

Ứng dụng chỉ đóng vai trò đối tượng triển khai; trọng tâm là pipeline CI/CD.

## Chạy trên máy (Windows, PowerShell)

```powershell
# 1. Bật PostgreSQL bằng Docker
docker compose up -d

# 2. Tạo môi trường ảo và cài thư viện
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 3. Tạo file cấu hình
copy .env.example .env

# 4. Chạy ứng dụng
uvicorn app.main:app --reload
```

Mở http://localhost:8000/health (kết quả mong đợi: `{"status":"ok","database":"connected"}`) và http://localhost:8000/docs.

## Chạy test

```powershell
pytest -v
```

## Tiến độ

- [x] Tuần 1: môi trường, khung ứng dụng, workflow đầu tiên
