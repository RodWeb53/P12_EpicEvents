from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models.base import Base


class Contract(Base):
    __tablename__ = 'contract'

    contract_id = Column(Integer, primary_key=True)
    contract_amount = Column(Float)
    due_payment = Column(Float)
    contract_status = Column(Boolean)
    creation_date = Column(DateTime, default=func.now(), nullable=False)
    update_date = Column(DateTime, default=func.now(), nullable=False)
    client_id = Column(Integer, ForeignKey('client.client_id', ondelete="SET NULL"))
    client = relationship("Client", back_populates="contract", lazy="subquery")
    event = relationship("Event", back_populates="contract", lazy="subquery")

    def __str__(self):
        return (
            f"Contract(contract_id='{self.contract_id}',"
            f"contract_amount='{self.contract_amount}',"
            f"due_payment='{self.due_payment}',"
            f"contract_status='{self.contract_status}',"
            f"creation_date='{self.creation_date}',"
            f"update_date='{self.update_date}',"
            f"client_id='{self.client_id}',"
            f"client='{self.client}',"
        )
