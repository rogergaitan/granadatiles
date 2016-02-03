import requests

def check_recaptcha_response(recaptcha_response):
    payload = {'secret': '6LdcMRcTAAAAALv7QYt4PM8qzaCP3COjiFRbDGvm',
               'response': recaptcha_response}
    r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                      data=payload)
    if r.json()['success']:
        return True
    else:
        return False
