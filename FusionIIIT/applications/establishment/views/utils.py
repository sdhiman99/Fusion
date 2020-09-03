# UTILITY FUNCTIONS
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from applications.globals.models import ExtraInfo, HoldsDesignation, Designation, DepartmentInfo
from notification.views import establishment_notif
from datetime import datetime
from applications.establishment.models import *
from applications.establishment.forms import *


def initial_checks(request):
    return {}


def is_admin(request):
    return request.user == Establishment_variables.objects.first().est_admin


def get_admin():
    return Establishment_variables.objects.first().est_admin


def is_eligible(request):
    return True


def is_fm(dictx):
    for key in dictx.keys():
        if 'fm_' in key:
            return True
    return False


def is_cpda(dictx):
    for key in dictx.keys():
        if 'cpda' in key:
            return True
    return False


def is_ltc(dictx):
    for key in dictx.keys():
        if 'ltc' in key:
            return True
    return False

