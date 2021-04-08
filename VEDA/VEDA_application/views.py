from django.shortcuts import render
from . import models

def template(request):
    return render(request, 'temp.html', context= {
        'groups': models.Group.objects.all()
    })