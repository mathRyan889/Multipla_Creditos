from django.shortcuts import render, redirect
import requests
import json
from .forms import RegisterLeadForm
import os

# Mantenha a função de notificação aqui
def send_pushbullet_notification(lead):
    # Seu token pessoal (Cuidado ao compartilhar este código publicamente)
    access_token = os.getenv('PUSHBULLET_TOKEN')
    url = "https://api.pushbullet.com/v2/pushes"
    
    payload = {
        "type": "note",
        "title": "🔥 Novo Lead Capturado",
        "body": (
            f"Nome: {lead.name}\n"
            f"Serviço: {lead.services.type_service}\n"
            f"Whats: {lead.whatsapp}\n"
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
        print(f"Erro ao enviar notificação: {e}")

def home(request):
    if request.method == 'POST':
        form = RegisterLeadForm(request.POST)
        if form.is_valid():
            # 1. Salva o lead no banco de dados
            novo_lead = form.save()
            
            # 2. CHAMA A NOTIFICAÇÃO (Faltava este passo!)
            send_pushbullet_notification(novo_lead)
            
            # 3. Redireciona para limpar o form
            return redirect('home') 
    else:
        form = RegisterLeadForm()
    
    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')