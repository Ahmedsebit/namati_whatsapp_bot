import os
import json
from flask import Blueprint, request, jsonify, current_app
from namati.services import respond
from namati.repositories import healthcheck_db

namati_v1_api_bp = Blueprint(
    'namati_v1_api_bp', __name__,
)


@namati_v1_api_bp.route('/api/receive_message', methods=['POST'])
def receive_message_api():
    data = request.data
    response = respond(data)
    return response
