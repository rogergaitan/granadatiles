from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from apps.portfolio.views import login_portfolio_user, portfolio_home, login_for_portfolio, register_user, logout_portfolio_user, portfolio_layouts, portfolio_create_layout

urlpatterns = [
        url(r'account/signup/$', register_user, name='signup_to_portfolio'),
        url(r'login$', login_for_portfolio, name='login_to_portfolio'),
        url(r'account/login/$', login_portfolio_user, name='login_user'),
        url(r'account/logout/$', logout_portfolio_user, name='logout_user'),
        url(_(r'layouts$'), portfolio_layouts, name='layouts'),
        url(_(r'layouts/create$'), portfolio_create_layout, name='create-layout'),
        url(_(r'$'), portfolio_home, name='home') ,
        ]