from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        link = eliminar_protocolo(link)
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
        
def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)

def eliminar_protocolo(url):
    protocolos = ["https://", "http://"]  # Agrega otros protocolos si es necesario
    for protocolo in protocolos:
        if url.startswith(protocolo):
            return url[len(protocolo):]  # Elimina el protocolo de la URL
    return url  # Si no se encuentra ningún protocolo, se devuelve la URL original sin cambios
