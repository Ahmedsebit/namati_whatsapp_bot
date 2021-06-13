from app.resources.items import namati_items


def respond(message, namati_items):
    
    message = message.lower()
    
    if 'what' in message and 'is'  in message and 'namati' in message:
        return namati_items.get('what_is_namati')
    if 'citizenship' in message and 'justice' in message and  'partners' in message:
        return
    if 'land' in message and 'environmental' in message and 'justicepartners' in message: 
        return namati_items.get('land_environmental_justicepartners')
    if 'impact' in message:
        return namati_items.get('impact')
    if 'injustices' in message:
        return namati_items.get('injustices')
    if 'citizenship' in message and 'justice' in message:
        return namati_items.get('citizenship_justice')
    if 'land' in message and 'environmental' in message and 'justice' in message:
        return namati_items.get('land_environmental_justice')     
    if 'health' in message and 'justice' in message:
        return namati_items.get('health_justice')
    if 'legal' in message and 'empowerment' in message and 'programs' in message:
        return namati_items.get('legal_empowerment_programs')
    if 'what' in message and 'we' in message and 'do' in message:
        return namati_items.get('what_we_do')
    if 'grassroots' in message and 'legal' in message and 'empowerment' in message:
        return namati_items.get('grassroots_legal_empowerment')
    if 'recognition' in message:
        return namati_items.get('recognition')
    if 'our' in message and 'mission' in message:
        return namati_items.get('our_mission')
    if 'meaning' in message:
        return namati_items.get('meaning')