import subprocess

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
@require_POST
def github_webhook(request):
    print(request.META)
    cmd = ''
    return HttpResponse('pong')
