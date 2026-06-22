from schemas.session import Session

sessions = {}

def get_session(user_id:str)->Session:
    if user_id not in sessions:
        sessions[user_id] = Session()

    return sessions[user_id]