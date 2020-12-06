from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime


def main(request):
    return render(request, 'main1.html', {'parameter': "test"})


def health(request):
    response = {'date': datetime.now().strftime("%d-%m-%Y %H:%M"),
                'current_page': request.build_absolute_uri(),
                'server_info':
                    {
                        'OS Name': os.name,
                        'User name': os.getlogin(),
                     },
                'client_info':
                    {
                        'User agent': request.headers['user-agent'],
                        'Remote address': request.META['REMOTE_ADDR'],
                        'Host Header': request.META['HTTP_HOST'],
                        'Remote host': request.META['REMOTE_HOST'],

                    }
                }
    return JsonResponse(response)