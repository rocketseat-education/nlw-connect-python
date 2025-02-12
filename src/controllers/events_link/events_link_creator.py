from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.eventos_link_repository import EventosLinkRepositoryInterface

class EventsLinkCreator:
    def __init__(self, events_link_repo: EventosLinkRepositoryInterface):
        self.__events_link_repo = events_link_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        event_link_info = http_request.body["data"]
        event_id = event_link_info["event_id"]
        subscriber_id = event_link_info["subscriber_id"]

        self.__check_event_link(event_id, subscriber_id)
        new_link = self.__create_event_link(event_id, subscriber_id)
        return self.__format_response(new_link, event_id, subscriber_id)

    def __check_event_link(self, event_id: int, subscriber_id: int) -> None:
        response = self.__events_link_repo.select_events_link(event_id, subscriber_id)
        if response: raise Exception("Link Already Exists!")

    def __create_event_link(self, event_id: int, subscriber_id: int) -> str:
        new_link = self.__events_link_repo.insert(event_id, subscriber_id)
        return new_link

    def __format_response(self, new_link: str, event_id: int, subscriber_id: int) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "Event Link",
                    "count": 1,
                    "attributes": {
                        "link": new_link,
                        "event_id": event_id,
                        "subscriber_id": subscriber_id
                    }
                }
            },
            status_code=201
        )
