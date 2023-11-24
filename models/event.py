from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models.base import Base


class Event(Base):
    __tablename__ = 'event'

    event_id = Column(Integer, primary_key=True)
    event_title = Column(String(255))
    start_date = Column(DateTime, default=func.now(), nullable=False)
    end_date = Column(DateTime, default=func.now(), nullable=False)
    location = Column(String(255))
    attendees = Column(Integer)
    notes = Column(String(1000))
    creation_date = Column(DateTime, default=func.now(), nullable=False)
    update_date = Column(DateTime, default=func.now(), nullable=False)
    support_id = Column(Integer, ForeignKey('custom_users.id', ondelete="SET NULL"))
    contact_support = relationship("CustomUser", back_populates="support", lazy="subquery")
    contract_id = Column(Integer, ForeignKey("contract.contract_id", ondelete="SET NULL"))
    contract = relationship("Contract", back_populates="", lazy="subquery")

    def __str__(self):
        return (
            f"Event(event_id='{self.event_id}',"
            f"event_title='{self.event_title}',"
            f"start_date='{self.start_date}',"
            f"end_date='{self.end_date}',"
            f"creation_date='{self.creation_date}',"
            f"update_date='{self.update_date}',"
            f"support_id='{self.support_id}',"
            f"contact_support='{self.contact_support}',"
            f"contract_id='{self.contract_id}',"
            f"contract='{self.contract}',"
        )
