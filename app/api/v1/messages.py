import os
import json
from flask import Blueprint, request, jsonify, current_app
from app.services import respond, sessions
from app.services.whatsapp import send_whatsapp
from app.repositories import healthcheck_db


namati_v1_api_bp = Blueprint(
    'namati_v1_api_bp', __name__,
)


@namati_v1_api_bp.route('/api/receive_message', methods=['POST'])
def receive_message_api():
    data = request.data
    response = respond(data['Body'])
    send_whatsapp(data['To'], response, data['From'])
    return response


@namati_v1_api_bp.route('/api/chat', methods=['POST'])
def chat_api():
    data = request.data
    phone_number = data.get('phone_number', None)
    message = data.get('message', None)
    response = sessions(phone_number, message)
    return response


@namati_v1_api_bp.route('/api/citizenship_chat', methods=['POST'])
def citizenhsip_chat_api():
    
    data = request.data
    message = data['Body']
    sender = data['From']
    recipient = data['To']
    
    phone_number = data.get('phone_number', None)
    response = sessions(phone_number, message)
    send_whatsapp(recipient, response, sender)
    return response