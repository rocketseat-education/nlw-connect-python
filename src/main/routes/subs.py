from flask import Blueprint, jsonify, request

subs_route_bp = Blueprint("subs_route", __name__)

from src.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subcribers_creator_validator

from src.model.repositories.subscribers_repository import SubscribersRepository

from src.controllers.subscribers.subscribers_creator import SubscribersCreator
from src.controllers.subscribers.subscribers_manager import SubscriberManager

@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_subs():
    subcribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    subs_repo = SubscribersRepository()
    subs_creator = SubscribersCreator(subs_repo)

    http_response = subs_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code


@subs_route_bp.route("/subscriber/link/<link>/event/<event_id>", methods=["GET"])
def subscribers_by_link(link, event_id):
    subs_repo = SubscribersRepository()
    subs_manager = SubscriberManager(subs_repo)

    http_request = HttpRequest(param={ "link": link, "event_id": event_id })

    http_response = subs_manager.get_subscribers_by_link(http_request)

    return jsonify(http_response.body), http_response.status_code

@subs_route_bp.route("/subscriber/ranking/event/<event_id>", methods=["GET"])
def link_ranking(event_id):
    subs_repo = SubscribersRepository()
    subs_manager = SubscriberManager(subs_repo)

    http_request = HttpRequest(param={ "event_id": event_id })

    http_response = subs_manager.get_event_ranking(http_request)

    return jsonify(http_response.body), http_response.status_code

