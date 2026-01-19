from django.shortcuts import render, redirect
import requests
import json
from .forms import RegisterLeadForm

def home(request):
    if request.method == 'POST':
        form = RegisterLeadForm(request.POST)
        if form.is_valid():
            form.save()
            # O redirect é essencial para limpar o form e recarregar a lista do banco
            return redirect('home') 
    else:
        form = RegisterLeadForm()
    
    return render(request, 'home.html', {'form': form})

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')



def send_pushbullet_notification(lead):
    access_token = "o.StnBdNNyn3FGPDhDTB3sHBgBp4QJZRE6"
    url = "https://api.pushbullet.com/v2/pushes"
    
    payload = {
        "type": "note",
        "title": "🔥 Novo Lead Capturado",
        "body": f"Nome: {lead.name}\nServiço: {lead.services.type_service}\nWhats: {lead.whatsapp}"
    }
    
    headers = {
        "Access-Token": access_token,
        "Content-Type": "application/json"
    }
    
    requests.post(url, data=json.dumps(payload), headers=headers)