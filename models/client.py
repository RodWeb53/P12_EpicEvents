from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models.base import Base


class Client(Base):
    __tablename__ = 'client'

    client_id = Column(Integer, primary_key=True)
    full_name = Column(String(255))
    email = Column(String(255), nullable=False)
    phone = Column(String(15))
    company_name = Column(String(255))
    creation_date = Column(DateTime, default=func.now(), nullable=False)
    update_date = Column(DateTime, default=func.now(), nullable=False)
    commercial_id = Column(Integer, ForeignKey('custom_users.id', ondelete="SET NULL"))
    contact_commercial = relationship("CustomUser", back_populates="commercial", lazy="subquery")
    contract = relationship("Contract", back_populates="client")

    def __str__(self):
        return (
            f"Client(client_id='{self.client_id}',"
            f"full_name='{self.full_name}',"
            f"email='{self.email}',"
            f"phone='{self.phone}',"
            f"company_name='{self.company_name}',"
            f"creation_date='{self.creation_date}',"
            f"update_date='{self.update_date}',"
            f"commercial_id='{self.commercial_id}',"
            f"contact_commercial='{self.contact_commercial}',"
        )
