import hmac
from hashlib import sha1
import subprocess

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.conf import settings
from django.utils.encoding import force_bytes

import requests
from ipaddress import ip_address, ip_network


@csrf_exempt
@require_POST
def github_webhook(request):
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')

    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')

    # If request reached this point we are in a good shape
    # Process the GitHub events
    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')

    if event == 'ping':

        return HttpResponse('pong')
    elif event == 'push':
        # Deploy some code for example

        cmd_git_pull = "cd {}; git pull;".format(settings.GIT_ROOT)
        cmd_gunicorn_restart = "cd {}; {}/bin/supervisorctl restart gunicorn".format(
            settings.SUPERVISOR_ROOT, settings.GIT_ROOT
        )
        output_1 = subprocess.check_output(cmd_git_pull, shell=True, stderr=subprocess.STDOUT)
        output_2 = subprocess.check_output(cmd_gunicorn_restart, shell=True, stderr=subprocess.STDOUT)
        return HttpResponse(output_1 + " | " + cmd_gunicorn_restart + " : " + output_2)

        # In case we receive an event that's not ping or push

    return HttpResponse(status=204)
