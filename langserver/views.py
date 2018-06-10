from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from subprocess import call, Popen, PIPE
import json
# Create your views here.
@csrf_exempt
def compilecode(request):
    with open('ccode.c','w+') as mycode:
        mycode.write(request.POST.get('code'))
    ccompile = Popen(["gcc","ccode.c"], stderr=PIPE)
    ccompileerr = ccompile.communicate()[1].decode()
    if ccompileerr != '':
        return JsonResponse({"success": ccompileerr})
    runoutput = Popen(["./a.out"], stdout=PIPE)
    output = runoutput.communicate()[0]
    call(["rm","ccode.c", "a.out"])
    return JsonResponse({"success": output.decode()})