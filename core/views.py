from django.shortcuts import render
from django.contrib import messages
from core.models import Email
from django.http import HttpResponse, HttpResponseRedirect
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def example(request):
    if request.method == 'POST':
        email = request.POST['email']
        if email == '' or re.match(EMAIL_REGEX, email) is None:
            messages.error(request, "뭔가 잘못됨! 확인해라, 이메일!")
            return HttpResponseRedirect(request.path)

        Email.objects.create(email=request.POST['email'], submitted_from=request.path)
        messages.success(request, "성공적으로 저장!")
        return HttpResponseRedirect(request.path)

    return render(request, 'core/example.html')

def beanjari(request):
    if request.method == 'POST':
        email = request.POST['email']
        if email == '' or re.match(EMAIL_REGEX, email) is None:
            messages.error(request, "뭔가 잘못됨! 확인해라, 이메일!")
            return HttpResponseRedirect(request.path)

        Email.objects.create(email=request.POST['email'], submitted_from=request.path)
        messages.success(request, "성공적으로 저장!")
        return HttpResponseRedirect(request.path)

    return render(request, 'core/beanjari.html')


def beanjari(request):
    if request.method == 'POST':
        email = request.POST['email']
        if email == '' or re.match(EMAIL_REGEX, email) is None:
            messages.error(request, "이메일 형식을 다시 확인해주세요😂")
            return HttpResponseRedirect(request.path)

        Email.objects.create(email=request.POST['email'], submitted_from=request.path)
        messages.success(request, "이메일이 성공적으로 저장되었어요!😁")
        return HttpResponseRedirect(request.path)

    return render(request, 'core/beanjari/beanjari.html')
