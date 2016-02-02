from django.contrib.auth.models import User

class AuthenticationService(object):
    def register_user(userdata):
        user_email = userdata.get('user')
        user = User.objects.create_user(user_email,
                                        email=user_email,
                                        password=userdata.get('password'))
