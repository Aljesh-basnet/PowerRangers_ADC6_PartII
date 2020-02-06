from django.shortcuts import render
from .models import ranger
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create or View ranger 
@csrf_exempt
def rangerDetail(request):
    if request.method == "GET":
        peka=ranger.objects.all()
        peka1=list(peka.values("cname","roomtype","cemail"))
        peka3={"ProductDetails":peka1}
        return JsonResponse(peka3)

    elif request.method == "POST":
        print(request.body)
        peka4=json.loads(request.body)
        ranger.objects.create(cname=peka4['Cname'],
        roomtype=peka4['room'],
        cemail=peka4['mail'])
        return JsonResponse({"message":"data posted successfully"})

# View, Delete, up specific ranger by Id
@csrf_exempt
def rangerUpDe(request,Id):
        peka5=ranger.objects.get(id=Id)
        if request.method == "GET":
            return JsonResponse({
            "cname":peka5.cname,
            "roomtype":peka5.roomtype,
            "cemail":peka5.cemail})
        

        elif request.method == "DELETE":
      
            peka5.delete()
            return JsonResponse({"message":"Deleted"})
            
            
                
        
        elif request.method == "PUT":
            up=json.loads(request.body) 
            peka5.cname=up['Cname']
            peka5.roomtype=up['room'] 
            peka5.cemail=up['mail']
            peka5.save()
            return JsonResponse({"message":"Updated"})





    




