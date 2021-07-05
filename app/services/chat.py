import emoji
from app.resources.items import namati_items
from app.repositories import (
                                get_user_session, 
                                update_level_session, 
                                add_user, 
                                get_user, 
                                add_session, 
                                update_journey_session,
                                end_session
                            )

p_emoji = emoji.emojize(':thumbs_up:')
cp_emoji = emoji.emojize(':clapping_hands:')
ke_emoji = emoji.emojize(':kenya_flag:')
df_emoji = emoji.emojize(':disappointed_face:')

citizenship = {
    'kenyan_parents':{
        'yes': True,
        'no' :{
            'born_in_kenya':{
                'yes': True,
                'no' :{
                    'married_to_kenyan':{
                        'no':False,
                        'yes':{
                            'more_than_7_years':{
                                'yes': True,
                                'no' : False
                            }
                        }
                    }
                }
            }
        }
    }
}


id_qualification = [
                        'Are you above 18 years', 
                        'Are you a Kenyan Citizen', 
                        'Do you have proof of age', 
                        'Do you have proof that either of the parents is a Kenyan'
                    ]


id_application_documents = [
                                'Are you above 18 years',
                                'Are you a Kenyan Citizen',
                                'Do you have your original birth certiﬁcate and a copy of the same',
                                'Do you have your school leaving certiﬁcate',
                                'Do you have your original national identity cards of both parents'
                        ]
 
kenyan_citizenship = [
                        'Are any of your parents a Kenyan citizen',
                        'Were you born in Kenya',
                        'Are you married to a Kenyan',
                        'Have you been married for more than 7 years'
                    ]

main_message = '''What would you like to do:\nUnderstand if If I’m a Kenyan citizen\nUnderstand if I qualify for an ID\nUnderstand the what I need to apply for an ID\nUnderstand the process of applying for an ID Card'''
                
welcome_message = '''Welcome to chat with us at namati.'''
                
                
id_application_process_message = [
'Upon the age of 18, the applicant should present himself to the nearest application centre either the district commissioner’s office or Huduma Centre',
'For certain communities you might need to begin with the village elders or chief',
'The applicant should go to the office of the District Officer to get a form with which they apply for the national identity card.',
'The applicant should then ﬁll out the details on the form that concerns them without any errors.',
'They should then take the form to the assistant chief or the chief for signing',
'The form should be taken to the office of the District officer where the details on the ﬁlled form are scrutinized and veriﬁed.',
'The District officer then appends a signature to the form.',
'If the form passes this stage, ﬁnger prints and a passport size photograph of the applicant are taken to be sent together with the form to the relevant offices mandated with the creation of the national identity cards.',
'The applicant is then issued with a waiting card with which they can use as the national identity card as they wait for their national identity card to be processed.',
'The waiting period may last up to two one year.',
'Check after at least two months to see if the ID is issued.'
]

def respond(message):
    
    message = message.lower()
    
    if 'what' in message and 'is'  in message and 'namati' in message:
        return namati_items.get('what_is_namati')
    elif 'citizenship' in message and 'justice' in message and  'partners' in message:
        return
    elif 'land' in message and 'environmental' in message and 'justice' in message and 'partners' in message: 
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
    elif 'mission' in message:
        return namati_items.get('our_mission')
    elif 'meaning' in message:
        return namati_items.get('meaning')
    else:
        return namati_items.get('questions_lists')


def sessions(phone_number, message):
    message = message.lower()
    if get_user(phone_number):
        user_session = get_user_session(phone_number)
        
        if user_session is None:
            add_session(phone_number, 0)
            return main_message
            
        if user_session['status'] == 'Inactive':
            add_session(phone_number, 0)
            return main_message
        
        if user_session['journey'] == None:
            if 'kenyan'in message and 'citizen' in message:
                update_journey_session(phone_number, 'citizenship')
                return citizenship(phone_number, message)
            elif 'qualify' in message and 'id' in message:
                update_journey_session(phone_number, 'id_qualification')
                return qualification(phone_number, message)
            elif 'need' in message and 'apply' in message and 'id' in message:
                update_journey_session(phone_number, 'id_application_documents')
                return application_documents(phone_number, message)
            elif 'process' in message and 'apply' in message and 'id' in message:
                update_journey_session(phone_number, 'id_process')
                return id_application_process(phone_number, message)
            else:
                return f'please choose from the given option\n{main_message}'
            
        elif user_session['journey'] == 'id_qualification':
            return qualification(phone_number, message)
        elif user_session['journey'] == 'id_application_documents':
            return application_documents(phone_number, message)
        elif user_session['journey'] == 'citizenship':
            return citizenship(phone_number, message)
        elif user_session['journey'] == 'id_process':
            return id_application_process(phone_number, message)

    else:
        add_user(phone_number)
        add_session(phone_number, 0)
        return f'{welcome_message}\n{main_message}'


def qualification(phone_number, response):
    
    user_session = get_user_session(phone_number)
    message = id_qualification[user_session['level']]
    p_emoji = emoji.emojize(':thumbs_up:')
    if user_session['level'] == len(id_qualification)-1:
        if user_session['results'] == True:
            if 'no' in response:
                update_level_session(phone_number, False)
                end_session(phone_number)
                return "Sorry {df_emoji}{df_emoji}{df_emoji}\nYou need to be a kenyan, above 18 with proof of age and have parents citizenship proof to qualify for a Kenyan ID"
            elif 'yes' in response:
                update_level_session(phone_number, True) 
                end_session(phone_number)
                return "Congratulations {cp_emoji}{cp_emoji}{cp_emoji}\nYou qualify for a Kenyan ID"
            else:
                return f"Please answer as yes or no\n {message}"
        elif user_session['results'] == False:
            if 'no' not in response or 'yes' not in response:
                update_level_session(phone_number, False)
                return "Sorry {df_emoji}{df_emoji}{df_emoji}\nYou need to be a kenyan, above 18 with proof of age and have parents citizenship proof to qualify for a Kenyan ID"
            else:
                return f"Please answer as yes or no\n {message}"
    else:
        if 'no' in response:
            update_level_session(phone_number, False)
            return f"Great {p_emoji}\n{message}" 
        elif 'yes' in response:
            update_level_session(phone_number, True)
            return f"Great {p_emoji}\n{message}" 
        else:
            if user_session['level'] == 0:
                if 'no' in response:
                    update_level_session(phone_number, False)
                    return f"Great {p_emoji}\n{message}" 
                elif 'yes' in response:
                    update_level_session(phone_number, True)
                    return f"Great {p_emoji}\n{message}" 
            return f"Please answer as yes or no\n {message}" 

    
def application_documents(phone_number, response):
    
    user_session = get_user_session(phone_number)
    message = id_application_documents[user_session['level']]
    p_emoji = emoji.emojize(':thumbs_up:')
    
    if user_session['level'] == len(id_application_documents)-1:
        if user_session['results'] == True:
            if 'no' in response:
                update_level_session(phone_number, False)
                end_session(phone_number)
                return f"Sorry {df_emoji}{df_emoji}{df_emoji}\nYou need to be a kenyan, above 18 with proof of age and have parents citizenship proof to apply for id"
            elif 'yes' in response:
                update_level_session(phone_number, True) 
                end_session(phone_number)
                return f"Congratulations {cp_emoji}{cp_emoji}{cp_emoji}\nYou qualify to get a Kenyan ID"
            else:
                return f"Please answer as yes or no\n {message}"
        elif user_session['results'] == False:
            if 'no' not in response or 'yes' not in response:
                update_level_session(phone_number, False)
                end_session(phone_number)
                return f"Sorry {df_emoji}{df_emoji}{df_emoji}\nYou need to be a kenyan, above 18 with proof of age and have parents citizenship proof to apply for id"
            else:
                return f"Please answer as yes or no\n {message}"
    else:
        if 'no' in response:
            update_level_session(phone_number, False)
            
            return f"Great {p_emoji}\n{message}" 
        elif 'yes' in response:
            update_level_session(phone_number, True)
            return f"Great {p_emoji}\n{message}" 
        else:
            if user_session['level'] == 0:
                if 'no' in response:
                    update_level_session(phone_number, False)
                    return f"Great {p_emoji}\n{message}" 
                elif 'yes' in response:
                    update_level_session(phone_number, True)
                    return f"Great {p_emoji}\n{message}" 
            return f"Please answer as yes or no\n {message}" 


def citizenship(phone_number, response):
    
    user_session = get_user_session(phone_number)
    
    if user_session['level'] == len(kenyan_citizenship):
        message = kenyan_citizenship[user_session['level']-1]
        if 'no' in response:
            update_level_session(phone_number, False)
            end_session(phone_number)
            return f"Sorry {df_emoji}{df_emoji}{df_emoji}\nYou do not qualify for Kenyan Citizenship"
        elif 'yes' in response:
            update_level_session(phone_number, True) 
            end_session(phone_number)
            return f"Congratulations {cp_emoji}{cp_emoji}{cp_emoji}\nYou do qualify for Kenyan Citizenship"
        else:
            return f"Please answer as yes or no\n {message}"
    elif user_session['level'] == len(kenyan_citizenship)-1:
        message = kenyan_citizenship[user_session['level']]
        if 'no' in response:
            update_level_session(phone_number, False)
            end_session(phone_number)
            return f"Sorry {df_emoji}{df_emoji}{df_emoji}\nYou do not qualify for Kenyan Citizenship"
        elif 'yes' in response:
            update_level_session(phone_number, True)
            return f"Great {p_emoji}\n{message}" 
        else:
            return f"Please answer as yes or no\n {message}"
    else:
        message = kenyan_citizenship[user_session['level']]
        if 'no' in response:
            update_level_session(phone_number, False)
            return f"Great {p_emoji}\n{message}" 
        elif 'yes' in response:
            update_level_session(phone_number, True)
            end_session(phone_number)
            cp_emoji = emoji.emojize(':clapping_hands:')
            return f"Congratulations {cp_emoji}{cp_emoji}{cp_emoji}\nYou do qualify for Kenyan Citizenship"
        else:
            if user_session['level'] == 0:
                if 'no' in response:
                    update_level_session(phone_number, False)
                    return f"Great {p_emoji}\n{message}" 
                elif 'yes' in response:
                    update_level_session(phone_number, True)
                    end_session(phone_number)
                    return f"Great {p_emoji}\n{message}" 
            return f"Please answer as yes or no\n {message}"


def id_application_process(phone_number, response):

    user_session = get_user_session(phone_number)
    message = "\n".join(id_application_process_message)
    end_session(phone_number)
    return message
    