from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class EventosLink(Base):
    __tablename__ = "Eventos_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer, ForeignKey("Eventos.id"))
    inscrito_id = Column(Integer, ForeignKey("Inscritos.id"))
    link = Column(String, nullable=False)
