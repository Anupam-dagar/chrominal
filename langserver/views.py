from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from subprocess import call, Popen, PIPE
import json
# Create your views here.
@csrf_exempt
def compilecode(request):
    import pdb; pdb.set_trace()
    with open('ccode.c','w+') as mycode:
        mycode.write(request.POST.get('code'))
    Popen(["gcc","ccode.c"])
    myvar = Popen(["./a.out"], stdout=PIPE)
    output = myvar.communicate()[0]
    print(output)
    Popen(["rm","ccode.c"])
    return JsonResponse({"success": output.decode()})