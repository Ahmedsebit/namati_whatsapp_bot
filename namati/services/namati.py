from namati.repositories import add_message
from namati.services.whatsapp import send_whatsapp


def receive_message(sender, body, recepients):
    
    response = send_whatsapp(sender, body, recepients)
    print(response.sid)
    add_message(response, response.sid, None)
    return 'response'
