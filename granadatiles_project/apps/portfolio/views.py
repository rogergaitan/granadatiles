from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import authenticate
from core.views import BaseViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

@require_GET
def login_for_portfolio(request):
    next = request.GET.get('next')
    return render(request, 'portfolio/portfolio_login.html',
                        {
                            'next': next,
                            'invalid_login': 'No'
                        })

def login_portfolio_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
           return render(request, 'portfolio/portfolio_login.html', 
                      {
                          'invalid_login': 'Yes',
                          'reason': _('Your account has been disabled')
                          })
    else:
        return render(request, 'portfolio/portfolio_login.html', 
                      {
                          'invalid_login': 'Yes',
                          'reason': _('Invalid Email or password')
                          })

@login_required(login_url='/portfolio/login')
def portfolio_home(request):
    return render(request , "portfolio/portfolio_index.html")

@api_view(['POST', ])
def register_user(request):
    result = {}
    print(request.data)
    return Response(result)



