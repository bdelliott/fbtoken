import datetime

from django.shortcuts import render_to_response
from django.template.context import RequestContext

def channel(request):
    context = RequestContext(request)
    response = render_to_response('tokenmanager/channel.html', context)

    # Cache the respons a long time:
    expire = 60*60*24*365
    response['Pragma'] = 'Public'
    response['Cache-Control'] = 'max-age=%d' % expire

    d = datetime.datetime.utcnow() + datetime.timedelta(seconds=expire)
    # ex: Expires: Thu, 01 Dec 1994 16:00:00 GMT
    response['Expires'] = d.strftime("%a, %d %b %Y %H:%M:%S GMT")
    return response

def index(request):
    context = RequestContext(request)
    return render_to_response('tokenmanager/index.html', context)

