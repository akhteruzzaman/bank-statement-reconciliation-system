from django.http import HttpResponse
from .models import Message

def hello_view(request):
    message = Message.objects.first()
    return HttpResponse(message.text if message else "No message found.")
