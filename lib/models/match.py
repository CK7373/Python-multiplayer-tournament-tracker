from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'))
    player_id = Column(Integer, ForeignKey('players.id'))

    tournament = relationship('Tournament', back_populates='matches')
    player = relationship('Player', back_populates='matches')

    def __repr__(self):
        return f"<Match(id={self.id}, tournament_id={self.tournament_id}, player_id={self.player_id})>"
