from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import Base


class CustomUser(Base):
    __tablename__ = 'custom_users'

    id = Column(Integer, primary_key=True)
    login = Column(String(25), unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(15))
    phone_mobile = Column(String(15))
    password = Column(String(255), nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean)
    role_id = Column(Integer, ForeignKey('role.id', ondelete="SET NULL"))
    role = relationship("Role", back_populates="employes", lazy="subquery")

    def __str__(self):
        return (f"CustomUser(id='{self.id}',"
                f"login='{self.login}',"
                f" first_name='{self.first_name}',"
                f" last_name='{self.last_name}',"
                f" email='{self.email}',"
                f" phone='{self.phone}',"
                f" phone_mobile='{self.phone_mobile}',"
                f" password='{self.password}',"
                f" is_staff='{self.is_staff}',"
                f" role_id='{self.role_id}',"
                f" role='{self.role}',"
                f" is_active='{self.is_active}',")

    def __repr__(self):
        return (f"CustomUser(id='{self.id}',"
                f" login='{self.login}',"
                f" first_name='{self.first_name}',"
                f" last_name='{self.last_name}',"
                f" email='{self.email}',"
                f" phone='{self.phone}',"
                f" phone_mobile='{self.phone_mobile}',"
                f" password='{self.password}',")
