import datetime
import logging

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson as json

from tokenmanager import models

logger = logging.getLogger(__name__)

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

def token(request):
    """Get or Set a token"""

    if request.method == "POST":
        logger.debug("Saving token")

        user_id = request.POST['userID']
        expires_in = int(request.POST['expiresIn'])
        access_token = request.POST['accessToken']

        expires = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)

        token = models.Token()
        token.token = access_token
        token.user_id = user_id
        token.expires = expires
        token.save()

        return HttpResponse(content="OK", content_type="text/plain")

    else:
        # just return latest token:
        user_id = request.GET['user_id']
        logger.info("Retrieving token for %s" % user_id)

        try:
            token = models.Token.objects.filter(user_id=user_id).latest('created')
            d = {"token": token.token,
                 "user_id": token.user_id, 
                 "expires": token.expires.strftime("%a %d %b %Y %H:%M:%S")}
            resp = json.dumps(d, sort_keys=True, indent=4)
            return HttpResponse(content=resp, content_type="application/json")
        except models.Token.DoesNotExist:
            d = {"error": "No token for user %s" % user_id}
            resp = json.dumps(d, sort_keys=True, indent=4)
            return HttpResponseNotFound(content=resp, content_type="application/json")

