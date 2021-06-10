def respond(data):
    
    message = data.get("message")
    
    if 'tesing' in message:    
        return f'Hi test currenly only'
    else:
        return f'Hi {message} received'
    