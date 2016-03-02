import requests, datetime, os

def check_recaptcha_response(recaptcha_response):
    payload = {'secret': '6LdcMRcTAAAAALv7QYt4PM8qzaCP3COjiFRbDGvm',
               'response': recaptcha_response}
    r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                      data=payload)
    if r.json()['success']:
        return True
    else:
        return False

def convert_to_boolean(value):
    if value == 'true':
        return True
    return False

''' This is so that django summernote keep the name of the image
     when is uploaded'''
def uploaded_filepath(instance, filename):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    return os.path.join('uploads', today, filename)