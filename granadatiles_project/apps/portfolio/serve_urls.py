from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from apps.portfolio.views import login_portfolio_user, portfolio_home, login_for_portfolio, register_user

urlpatterns = [
        url(r'account/signup/$', register_user, name='signup_to_portfolio'),
        url(r'login$', login_for_portfolio, name='login_to_portfolio'),
        url(r'account/login/$', login_portfolio_user, name='login_user'),
        url(_(r'$'), portfolio_home, name='home') ,
        ]