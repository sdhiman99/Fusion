from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from applications.globals.models import ExtraInfo, HoldsDesignation, Designation, DepartmentInfo
from notification.views import establishment_notif
from datetime import datetime

from applications.establishment.models import *
from applications.establishment.forms import *
from .utils import *
from .cpda import *
from .ltc import *
from .fm import *


@login_required(login_url='/accounts/login')
def establishment(request):
    response = {}
    # Check if establishment variables exist, if not create some fields or ask for them
    response.update(initial_checks(request))    

    if is_admin(request) and request.method == "POST": 
        if is_fm(request.POST):
            handle_fm_admin(request)
        if is_cpda(request.POST):
            handle_cpda_admin(request)
        if is_ltc(request.POST):
            handle_ltc_admin(request)

    if is_eligible(request) and request.method == "POST":
        if is_cpda(request.POST):
            handle_cpda_eligible(request)
        if is_ltc(request.POST):
            handle_ltc_eligible(request)

    ############################################################################

    if is_admin(request):
        response.update(generate_fm_admin_lists(request))
        response.update(generate_cpda_admin_lists(request))
        response.update(generate_ltc_admin_lists(request))
        return render(request, 'establishment/establishment.html', response)
    
    if is_eligible(request):
        response.update(generate_cpda_eligible_lists(request))
        response.update(generate_ltc_eligible_lists(request))
    
    return render(request, 'establishment/establishment.html', response)
