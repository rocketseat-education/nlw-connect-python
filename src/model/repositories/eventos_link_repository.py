import random
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos_link import EventosLink
from .interfaces.eventos_link_repository import EventosLinkRepositoryInterface

class EventosLinkRepository(EventosLinkRepositoryInterface):
    def insert(self, event_id: int, subscriber_id: int) -> str:
        with DBConnectionHandler() as db:
            try:
                link_final = ''.join(random.choices('0123456789', k=7))
                formatted_link = f'evento-{event_id}-{subscriber_id}-{link_final}'

                new_events_link = EventosLink(
                    evento_id=event_id,
                    inscrito_id=subscriber_id,
                    link=formatted_link
                )
                db.session.add(new_events_link)
                db.session.commit()

                return formatted_link
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_events_link(self, event_id: int, subscriber_id: int) -> EventosLink:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(EventosLink)
                .filter(
                    EventosLink.evento_id == event_id,
                    EventosLink.inscrito_id == subscriber_id
                )
                .one_or_none()
            )
            return data
