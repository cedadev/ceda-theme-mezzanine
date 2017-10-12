from django import template
from django.conf import settings

from url_tools.helper import UrlHelper
from dj_security_middleware.middleware import LOGOUT, login_service
from dj_security_middleware.middleware import get_userid_from_request,\
                                              get_openid_from_request
from dj_security_middleware.exception import DJMiddlewareException

from __builtin__ import True

DEFAULT_LOGIN_URL = 'https://auth.ceda.ac.uk/account/signin/'

# Template tags
register = template.Library()

@register.assignment_tag(takes_context=True)
def user_logged_in(context):
    '''Get the status of a user, return the userid if logged in'''
    request = context['request']
    return get_userid_from_request(request)

@register.assignment_tag(takes_context=True)
def get_userid(context):
    request = context['request']
    return get_userid_from_request(request)

@register.assignment_tag(takes_context=True)
def get_openid(context):
    request = context['request']
    return get_openid_from_request(request)

@register.simple_tag
def logout_url(url):
    url = UrlHelper(url)
    logout_kwarg = {LOGOUT: ''}
    try:
        url.update_query_data(**logout_kwarg)
        return url.get_full_path()
    except:
        return ''

@register.simple_tag
def login_url():
    try:
        return login_service()
    except DJMiddlewareException:
        return getattr(settings, 'SECURITY_LOGIN_SERVICE', DEFAULT_LOGIN_URL)