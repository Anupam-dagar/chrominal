from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from subprocess import call, Popen, PIPE
import json
# Create your views here.
@csrf_exempt
def compilec(request):
    with open('submission.c','w+') as mycode:
        mycode.write(request.POST.get('code'))
    ccompile = Popen(["gcc","submission.c"], stderr=PIPE)
    ccompileerr = ccompile.communicate()[1].decode()
    if ccompileerr != '':
        call(["rm","submission.c"])        
        return JsonResponse({"success": ccompileerr})
    runoutput = Popen(["./a.out"], stdout=PIPE)
    output = runoutput.communicate()[0]
    call(["rm","submission.c", "a.out"])
    return JsonResponse({"success": output.decode()})

@csrf_exempt
def compilecpp(request):
    with open('submission.cpp','w+') as mycode:
        mycode.write(request.POST.get('code'))
    ccompile = Popen(["g++","submission.cpp"], stderr=PIPE)
    ccompileerr = ccompile.communicate()[1].decode()
    if ccompileerr != '':
        return JsonResponse({"success": ccompileerr})
    runoutput = Popen(["./a.out"], stdout=PIPE)
    output = runoutput.communicate()[0]
    call(["rm","submission.cpp", "a.out"])
    return JsonResponse({"success": output.decode()}) 