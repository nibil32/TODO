from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ViewSet
from reminder.models import Task
from api.serializer import Taskserializer
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework import authentication,permissions

class Taskviewsetview(ViewSet):

    authentication_classes=[BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Task.objects.all()
        serializers=Taskserializer(qs,many=True)
        return Response(data=serializers.data)
    
    def create(self,request,*args,**kwargs):
        serializers=Taskserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(serializers.errors)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        if qs.user==request.user:
            qs.delete()
            return Response()
        return Response("login user doesnt match")
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializers=Taskserializer(qs)
        return Response(data=serializers.data)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        if qs.user==request.user:
            qs.update()
            return Response()
        return Response("not updated successfully")