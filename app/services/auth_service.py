# app/services/auth_service.py

def login_user(username: str, password: str):
    if username == "admin" and password == "1234":
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}