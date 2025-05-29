from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    matches = relationship('Match', back_populates='player')

    def __repr__(self):
        return f"<Player(id={self.id}, name='{self.name}')>"
