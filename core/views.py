from django.shortcuts import render
from django.contrib import messages
from core.models import Email
from django.http import HttpResponse, HttpResponseRedirect
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def fitster(request):
    if request.method == 'POST':
        email = request.POST['email']
        if email == '' or re.match(EMAIL_REGEX, email) is None:
            messages.error(request, "에러!")
            return HttpResponseRedirect(request.path)

        Email.objects.create(email=request.POST['email'], submitted_from=request.path)
        if email == 'heart@gmail.com':
            messages.success(request, "감사합니다!")
        if email == 'more@gmail.com' or email == 'heart@gmail.com':
            return render(request, 'core/fitsterL.html')
        
    return render(request, 'core/fitster.html')

def ffitster(request):
    if request.method == 'POST':
        email = request.POST['email']
        if email == '' or re.match(EMAIL_REGEX, email) is None:
            messages.error(request, "에러!")
            return HttpResponseRedirect(request.path)

        Email.objects.create(email=request.POST['email'], submitted_from=request.path)
        if email == 'fheart@gmail.com':
            messages.success(request, "감사합니다!")
        if email == 'fmore@gmail.com' or email == 'fheart@gmail.com':
            return render(request, 'core/ffitsterL.html')
        
    return render(request, 'core/ffitster.html')

