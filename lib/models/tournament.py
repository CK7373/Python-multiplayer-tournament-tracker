from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base

class Tournament(Base):
    __tablename__ = 'tournaments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    matches = relationship('Match', back_populates='tournament')

    def __repr__(self):
        return f"<Tournament(id={self.id}, name='{self.name}')>"
