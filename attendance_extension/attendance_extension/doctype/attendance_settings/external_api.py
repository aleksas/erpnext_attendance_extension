from datetime import datetime, date

def get_users_activites(external_api_root_url):
    stub_users_activites = [
        {'Email': 'username1@domain.com', 'LoginName':'username1'},
        {'Email': 'username1@domain.com', 'LoginName':'username1'},
        {'Email': 'username1@domain.com', 'LoginName':'username1'}
    ]
    
    return stub_users_activites

def get_user_map(external_api_root_url):
    acts =  get_users_activites(external_api_root_url)
    return { a['Email']:a['LoginName'] for a in acts if a['Email'] }, { a['LoginName']:a['Email'] for a in acts if a['LoginName'] } 

def get_events(external_api_root_url, username, dt):
    stub_events = [
        {'username': username, 'year': dt.year, 'month': dt.month, 'day': dt.day, 'year': dt.year, 'datetime':datetime.now(), 'status': 'Valid'},
        {'username': username, 'year': dt.year, 'month': dt.month, 'day': dt.day, 'year': dt.year, 'datetime':datetime.now(), 'status': 'Valid'},
        {'username': username, 'year': dt.year, 'month': dt.month, 'day': dt.day, 'year': dt.year, 'datetime':datetime.now(), 'status': 'Valid'},
        {'username': username, 'year': dt.year, 'month': dt.month, 'day': dt.day, 'year': dt.year, 'datetime':datetime.now(), 'status': 'Valid'},
        {'username': username, 'year': dt.year, 'month': dt.month, 'day': dt.day, 'year': dt.year, 'datetime':datetime.now(), 'status': 'Valid'},
        {'username': username, 'year': dt.year, 'month': dt.month, 'day': dt.day, 'year': dt.year, 'datetime':datetime.now(), 'status': 'Valid'}
    ]
    
    return stub_events

if __name__ == '__main__':
    external_api_root_url = 'http://external.api.address/'
    users_activites = get_users_activites(external_api_root_url)
    dt = date(year=2019, month=2, day=6)

    for users_activity in users_activites:
        username = users_activity['LoginName']
        events = get_events(external_api_root_url, username, dt)

        print (events)
