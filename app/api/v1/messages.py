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
    print(data)
    response = respond(data)
    send_whatsapp('+14155238886', response, '+254701874389')
    return response
