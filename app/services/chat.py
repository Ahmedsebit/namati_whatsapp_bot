from app.resources.items import namati_items


def respond(message):
    
    message = message.lower()
    
    if 'what' in message and 'is'  in message and 'namati' in message:
        return namati_items.get('what_is_namati')
    elif 'citizenship' in message and 'justice' in message and  'partners' in message:
        return
    elif 'land' in message and 'environmental' in message and 'justicepartners' in message: 
        return namati_items.get('land_environmental_justicepartners')
    elif 'impact' in message:
        return namati_items.get('impact')
    elif 'injustices' in message:
        return namati_items.get('injustices')
    elif 'citizenship' in message and 'justice' in message:
        return namati_items.get('citizenship_justice')
    elif 'land' in message and 'environmental' in message and 'justice' in message:
        return namati_items.get('land_environmental_justice')     
    elif 'health' in message and 'justice' in message:
        return namati_items.get('health_justice')
    elif 'legal' in message and 'empowerment' in message and 'programs' in message:
        return namati_items.get('legal_empowerment_programs')
    elif 'what' in message and 'we' in message and 'do' in message:
        return namati_items.get('what_we_do')
    elif 'grassroots' in message and 'legal' in message and 'empowerment' in message:
        return namati_items.get('grassroots_legal_empowerment')
    elif 'recognition' in message:
        return namati_items.get('recognition')
    elif 'our' in message and 'mission' in message:
        return namati_items.get('our_mission')
    elif 'meaning' in message:
        return namati_items.get('meaning')
    else:
        return namati_items.get('questions_lists')