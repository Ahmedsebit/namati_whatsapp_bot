import os
import json
from flask import Blueprint, request, jsonify, current_app
from app.services import respond 
from app.services.whatsapp import send_whatsapp
from app.repositories import healthcheck_db


namati_v1_api_bp = Blueprint(
    'namati_v1_api_bp', __name__,
)


@namati_v1_api_bp.route('/api/receive_message', methods=['POST'])
def receive_message_api():
    data = request.data
    print(data['To'], data['From'], data['Body'])
    response = respond(data['Body'])
    send_whatsapp(data['To'], response, data['From'])
    return response
