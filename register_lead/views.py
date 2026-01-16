from django.shortcuts import render, redirect
from .forms import RegisterLeadForm
from .models import Service  # Importe o modelo de Serviço

def home(request):
    if request.method == 'POST':
        form = RegisterLeadForm(request.POST)
        if form.is_valid():
            form.save()
            # É melhor usar redirect aqui para "limpar" o formulário após o envio
            return redirect('home') 
    else:
        # O Django usará o queryset definido no seu forms.py ou no model
        form = RegisterLeadForm()
    
    # IMPORTANTE: O formulário DEVE ser passado no contexto
    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')