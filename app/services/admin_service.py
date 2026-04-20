# app/services/admin_service.py

from sqlalchemy.orm import Session
from app.models.admin_model import AdminSponsor

def get_all_admins(db: Session):
    return db.query(AdminSponsor).all()

def create_admin(db: Session, data):
    new_admin = AdminSponsor(**data.model_dump())
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin