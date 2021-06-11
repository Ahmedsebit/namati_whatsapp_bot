from twilio.rest import Client
from flask import current_app, request, jsonify, Response


account_sid = current_app.config['TWILIO_ACCOUNT_SID']
auth_token = current_app.config['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def send_whatsapp(sender, message, recepients):
    
    response = client.messages.create(
                              from_=f'{sender}',
                              body=message,
                              to=f'{recepients}'
                          )
    return response 