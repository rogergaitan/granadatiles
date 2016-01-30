from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET

@require_GET
def login_for_portfolio(request):
    next = request.GET.get('next')
    return render(request, 'portfolio/portfolio_login.html',
                        {
                            'next': next
                        })

@require_POST
def login_portfolio_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
           return render(request, 'index.html', 
                      {
                          'invalid_login': True,
                          'reason': _('Your account has been disabled')
                          })
    else:
        return render(request, 'index.html', 
                      {
                          'invalid_login': True,
                          'reason': _('Invalid login')
                          })

@login_required(login_url='/portfolio/login')
def portfolio_home(request):
    return render(request , "portfolio/portfolio_index.html")

