import os
import requests
import json
from django.shortcuts import render, redirect
from .forms import RegisterLeadForm

def send_pushbullet_notification(lead):
    # Busca o token do arquivo .env
    access_token = os.getenv('PUSHBULLET_TOKEN')
    url = "https://api.pushbullet.com/v2/pushes"
    
    if not access_token:
        return

    payload = {
        "type": "note",
        "title": "🔥 Novo Lead: Múltipla Créditos",
        "body": (
            f"Nome: {lead.name}\n"
            f"Serviço: {lead.services.type_service}\n"
            f"WhatsApp: {lead.whatsapp}\n"
            f"CPF: {lead.cpf if lead.cpf else 'Não informado'}"
        )
    }
    
    headers = {
        "Access-Token": access_token,
        "Content-Type": "application/json"
    }
    
    try:
        requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
    except Exception as e:
        print(f"Erro Pushbullet: {e}")

def home(request):
    if request.method == 'POST':
        form = RegisterLeadForm(request.POST)
        if form.is_valid():
            novo_lead = form.save()
            send_pushbullet_notification(novo_lead)
            return redirect('home') 
    else:
        form = RegisterLeadForm()
    
    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')