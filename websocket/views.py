from django.shortcuts import render

# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import boto3
from .models import ChatMessage, ConnectionModel

@csrf_exempt
def test(request):
    return JsonResponse({'message': 'hello Daud'}, status=200)


def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(str(body_unicode))



@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    connectionid = ConnectionModel.objects.create(connection_id=connection_id)
    connectionid.save()
    return JsonResponse({'message': 'Connect Successfully'}, status=200)


@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    connectionid = ConnectionModel.objects.get(connection_id=connection_id)
    connectionid.delete()
    return JsonResponse({'message': 'Disconnect Successfully'}, status=200)